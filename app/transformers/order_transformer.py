from app.schemas import Order
from app.services.currency_service import CurrencyService

class OrderTransformer:
    def __init__(self, currency_service: CurrencyService):
        self.currency_service = currency_service

    def transform(self, order: Order, settings: dict) -> Order:
        # Transform order if needed (e.g., currency conversion)
        if order.currency == 'USD':
            order.price = self.currency_service.convert(order.price, 'USD', 'TWD', settings['exchange_rate'])
            order.currency = 'TWD'
        return order
