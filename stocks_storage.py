from stock import Stock


class StocksStorage:
    """
    class Storage

    Stores stock instances based on a set of symbols.

    Attributes:
        stocks dict: Stock instances based on given symbols.
    """

    def __init__(self, symbols: set[str]):
        """
        Initializes an instance of StocksStorage and generates Stocks instances.
        """
        self.stocks = {symbol: Stock(symbol) for symbol in symbols}
