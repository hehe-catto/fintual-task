from stocks_storage import StocksStorage
import random


class Portfolio:
    """
    class Portfolio

    Attributes:
        dict allocation: represents the distribution of stocks that the Portfolio is aiming {symbol: percentage in decimals}
        StocksStorage stocks_storage: stores stock instances
        dict total_per_stocks: Stores the number of stocks in the portfolio per stock.
        int max_number_shares:  Maximum limit for the initial number of stocks

    Methods:
        generate_stocks_number:  generates the initial number of actions randomly
        rebalance: rebalance the number of stocks based on the desired allocation
    """

    def __init__(
        self,
        allocation: dict,
        stocks_storage: StocksStorage,
        max_number_stocks: int = 1000,
    ):
        self.allocation = allocation
        self.stocks_storage = stocks_storage
        self.total_per_stock = {}
        # generate initial stocks number
        self.generate_stocks_number(max_number_stocks)
        # rebalance portfolio
        self.rebalance()

    def generate_stocks_number(self, max_number_stocks: int):
        """Generates the initial number of stocks per symbol, calculating a random value between 0 and attribute max_

        Returns:
               None
        """
        self.total_per_stock = {
            symbol: random.randint(0, max_number_stocks) for symbol in self.allocation
        }

    def rebalance(self):
        """Rebalance the number of stocks based on the assigned allocation, considering the latest price and the current number of stocks.

        Returns:
            dict: result that indicates per action the number of stocks to sell or buy
        """
        result = {}
        # calculate the the current value of the portfolio
        portfolio_value = 0
        for symbol in self.allocation:
            portfolio_value += (
                self.total_per_stock[symbol]
                * self.stocks_storage.stocks[symbol].current_price()
            )

        for symbol in self.allocation:
            latest_price = self.stocks_storage.stocks[symbol].latest_price
            # calculate current stock value in the portfolio
            actual_participation = self.total_per_stock[symbol] * latest_price
            # calculate desired stock value to fulfill the allocation
            needed_participation = self.allocation[symbol] * portfolio_value
            # number of stocks to sell/buy to rebalance the portfolio (rounded to the fourth decimal place)
            stocks_number = round(
                abs(actual_participation - needed_participation) / latest_price, 4
            )
            # update stocks number
            self.total_per_stock[symbol] = stocks_number

            # results
            if actual_participation == needed_participation:
                continue
            else:
                buy_or_sell = (
                    "SELL" if actual_participation > needed_participation else "BUY"
                )
            result[symbol] = {buy_or_sell: stocks_number}

        return result
