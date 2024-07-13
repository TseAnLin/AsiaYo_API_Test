class CurrencyService:
    def convert(self, amount: int, from_currency: str, to_currency: str, rate: float) -> int:
        # Convert currency
        if from_currency == 'USD' and to_currency == 'TWD':
            return int(amount * rate)
        raise ValueError(f"Unsupported currency conversion: {from_currency} to {to_currency}")
