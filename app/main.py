from fastapi import FastAPI, HTTPException, Depends
from app.schemas import Order, OrderResponse
from app.services.order_service import OrderService
from app.validators.order_validator import OrderValidator
from app.transformers.order_transformer import OrderTransformer
from app.services.currency_service import CurrencyService
from app.config import get_settings

app = FastAPI()

def get_currency_service():
    return CurrencyService()

def get_order_transformer(currency_service: CurrencyService = Depends(get_currency_service)):
    return OrderTransformer(currency_service)

@app.post("/api/orders", response_model=OrderResponse)
async def create_order(
    order: Order,
    settings: dict = Depends(get_settings),
    validator: OrderValidator = Depends(OrderValidator),
    transformer: OrderTransformer = Depends(get_order_transformer),
    order_service: OrderService = Depends(OrderService)
):
    # Main endpoint for order creation
    try:
        validated_order = validator.validate(order)
        transformed_order = transformer.transform(validated_order, settings)
        processed_order = order_service.process(transformed_order)
        return OrderResponse(**processed_order.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
