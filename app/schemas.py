from pydantic import BaseModel

class Address(BaseModel):
    city: str
    district: str
    street: str

class Order(BaseModel):
    # Order schema
    id: str
    name: str
    address: Address
    price: int
    currency: str

class OrderResponse(Order):
    # Response schema, inheriting from Order
    pass