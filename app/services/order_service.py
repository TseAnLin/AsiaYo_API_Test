from app.schemas import Order

class OrderService:
    # Service class for order validation and transformation.
    
    def process(self, order: Order) -> Order:
        '''
        Process the order.
        
        Converts USD to TWD if necessary.
        
        Args:
            order (Order): The order to be processed.

        Returns: 
            Order: The processed order.
        '''
        if order.currency == 'USD':
            order.price = int(order.price * 32.53)
            order.currency = 'TWD'
        return order
