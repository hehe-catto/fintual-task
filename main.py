from stocks_storage import StocksStorage
from portfolio import Portfolio

# Generate stocks storage
storage = StocksStorage({"AAPL", "META", "NVDA"})

# Generates stocks allocation {symbol: percentage}
allocation = {"AAPL": 0.40, "META": 0.40, "NVDA": 0.20}

# Portfolio instance with
portfolio_example = Portfolio(allocation=allocation, stocks_storage=storage)
print(portfolio_example.rebalance())
