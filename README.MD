# Fintual Task

## Summary
Python repository that rebalances a portfolio based on an initial allocation.

## Files
There are three main classes
1. `Stock`:  represents a stock, with its symbol, and calculates the latest price.
2. `StocksStorage`: it stores the stock instances.
3. `Portfolio`: represents a portfolio has an initial allocation when created, stores the number of shares per stock, and has the requested rebalancing method.


## Installation
Clone the repository and run the `main.py` file to print an example implementation.

## Implementation
Steps to follow to use the Portfolio rebalancing method.

First, create a Stocks Storage instance with the stock symbols that the portfolio will have.
```
# Generate stocks storage
storage = StocksStorage({"AAPL", "META", "NVDA"})
```

Second, instantiate the portfolio by assigning the created stocks storage and the allocation as attributes.
```
# Generates stocks allocation {symbol: percentage}
allocation = {"AAPL": 0.40, "META": 0.40, "NVDA": 0.20}

# Portfolio instance with
portfolio_example = Portfolio(allocation=allocation, stocks_storage=storage)
```

Finally, run the rebalancing method and print the results:
```
print(portfolio_example.rebalance())

>>> {'AAPL': {'BUY': 1410.1468}, 'META': {'SELL': 1181.2307}, 'NVDA': {'BUY': 1371.0924}}
```
## Assumptions

- Incorrect inputs are not handled
- The latest stock price is calculated randomly. More details about this are in the Stock class.
- The initial number of shares when creating a portfolio is also calculated randomly. More details about this are in the Portfolio class.
- Since the portfolio is created with a random number of stocks, the rebalancing method is executed when it is instantiated, so that it is balanced.

