import random

class Stock:
    """
    class Stock

    Attributes:
        str symbol: stock's identifier
        int max_price: stock's max price, default 100 (used in method current_price)
        int latest_price: stores stock's most recent price
        
    Methods:
        current_price: Returns stock latest available price
    """

    def __init__(self, symbol: str, max_price: int = 100):
        """Initializes an instance of Stock.
        """
        self.symbol = symbol
        self.max_price = max_price
        self.latest_price = self.current_price()

    def current_price(self) -> int:
        """Generates latest stock price, calculating a random value between 0 and attribute max_price.

        Returns:
            int: Latest stock's price
        """
        self.latest_price = random.randint(0, self.max_price)
        return self.latest_price
