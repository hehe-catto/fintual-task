# Fintual Task

## Summary
Python repository that rebalances a portfolio based on an initial allocation

## Installation
Clone the repository and run the `main.py` file to print an example implementation.

### Implementation
```
# Generate stocks storage
storage = StocksStorage({"AAPL", "META", "NVDA"})

# Generates stocks allocation {symbol: percentage}
allocation = {"AAPL": 0.40, "META": 0.40, "NVDA": 0.20}

# Portfolio instance with
portfolio_example = Portfolio(allocation=allocation, stocks_storage=storage)
print(portfolio_example.rebalance())

```
## Assumptions

- The latest stock price is calculated randomly. More details about this are in the Stock class.
- The initial number of shares when creating a portfolio is also calculated randomly. More details about this are in the Portfolio class.