from app.schemas import Order

class OrderValidator:
    def validate(self, order: Order) -> Order:
        # Validate order fields
        self._validate_name(order.name)
        self._validate_price(order.price)
        self._validate_currency(order.currency)
        return order

    def _validate_name(self, name: str):
        # Check if name is capitalized
        if not name.istitle():
            raise ValueError('Name is not capitalized')

    def _validate_price(self, price: int):
        # Check if price is within limit
        if price > 2000:
            raise ValueError('Price is over 2000')

    def _validate_currency(self, currency: str):
        # Check if currency is valid
        if currency not in ['TWD', 'USD']:
            raise ValueError('Currency format is wrong')