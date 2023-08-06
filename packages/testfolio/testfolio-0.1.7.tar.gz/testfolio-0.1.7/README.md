# testfolio
<a target="new" href="https://pypi.org/pypi/testfolio"><img border=0 src="https://img.shields.io/badge/python-3.6%2B-blue"></a>
<a target="new" href="https://pypi.org/pypi/testfolio"><img border=0 src="https://img.shields.io/pypi/dm/testfolio"></a>
<a target="new" href="https://pypi.org/pypi/testfolio"><img border=0 src="https://img.shields.io/pypi/v/testfolio"></a>
<a target="new" href="https://www.codefactor.io/repository/github/bradleyhe/testfolio"><img border=0 src="https://img.shields.io/codefactor/grade/github/BradleyHe/testfolio"></a>

Backtest and visualize your portfolio allocations using historical market data from Yahoo Finance.

## Quick Start
### Installation
You can install **testfolio** using pip:
``` {.sourceCode .bash}
$ pip install testfolio -U
```

### Requirements
**testfolio** depends on [yfinance](https://github.com/ranaroussi/yfinance) for retrieving market data; as such, the requirements match its requirements.
- [Python](https://www.python.org) \>= 3.6+
- [Pandas](https://github.com/pydata/pandas) \>= 1.0.0
- [Numpy](http://www.numpy.org) \>= 1.11.1
- [requests](http://docs.python-requests.org/en/master/) \>= 2.14.2
- [lxml](https://pypi.org/project/lxml/) \>= 4.5.1
- [Matplotlib](https://matplotlib.org/) \>= 3.5.0

### Example Usage
#### Creating a backtest
Stock tickers are specified in the allocation, along with their respective percent allocations. Rebalancing frequency, start date, and end date can also be specified.
```python
import testfolio as tsf

allocation_1 = {
    'SPY': 0.6,
    'TLT': 0.4
}

backtest_1 = tsf.Backtest(allocation_1, rebalance='q', name='60/40 Portfolio')
print(backtest_1)
```

#### Output
```text
------------------- Metrics -------------------
Name: 60/40 Portfolio
Allocation: {'SPY': 0.6, 'TLT': 0.4}
Starting Value: $1000.00
Ending Value: $5390.85
Start Date: 2002-07-30
End Date: 2022-07-15
CAGR: 8.80%
Maximum Drawdown: -30.48%
STD (annualized): 10.32%
Sharpe Ratio: 0.76
Sortino Ratio: 1.08
Market Correlation: 0.84
-----------------------------------------------
```

Options for creating the backtest can be seen below:
```python
backtest = Backtest(
            # Must be a dictionary with ticker keys corresponding to allocation percentages that sum to 1.
            allocation, 
    
            # Portfolios are rebalanced quarterly by default. Other options include 'd' (daily), 'w' (weekly),
            # 'm' (monthly), 'q' (quarterly), 'y' (yearly), and 'no' (no rebalancing). Rebalancing occurs on the first 
            # day of the specified interval.
            rebalance='q', 
            
            # Must be in YYYY-mm-dd string format. Set to the earliest possible date when all tickers existed by 
            # default. Will be rounded to the 1st of the next month.
            start_date='2020-01-01',
            
            # Must be in YYYY-mm-dd string format. Set to today by default. Will be rounded to the 1st of the last month.
            end_date='2022-03-02',
    
            # Set to 1000 by default.
            start_val=1000,
    
            # If True, then dividends are reinvested into its security. If False, then dividends generated are not 
            # incorporated into the portfolio.
            invest_dividends=False,
    
            # Set to "Portfolio n" where n is the nth portfolio made by default.
            name='Example Portfolio',
            
            # If True, adjusts all values and calculations to be real dollars based on the start date. Most recent 
            # months may not be adjusted if inflation data is not available.
            adj_inflation=False)
```
Aliases for broad market indices are available as well, and are set to the below mapping:
```python
ALIAS_TO_TICKER = {
    'S&P 500': 'VFINX',
    'Long Term Treasury': 'VUSTX',
    'Total US Bond Market': 'VBMFX',
    'Total US Stock Market': 'VTSMX',
    'Total Intl Stock Market': 'VGTSX',
    'Gold': 'GC=F',
    'Intermediate Term Treasury': 'IEF',
    'Short Term Treasury': 'VFISX',
    'REIT': 'VGSIX',
    'US Small Cap': 'NAESX',
    'US Mid Cap': 'VMCIX'
}
```
In addition to the attributes set during creation, Backtest objects have the following attributes and functions:

```python
backtest = Backtest(allocation)

# pandas DataFrame containing the value of the portfolio every month. Columns include each of the tickers, the total 
# portfolio value, and drawdown.
backtest.hist

# Maximum drawdown 
backtest.max_drawdown

# Compound annual growth rate 
backtest.cagr

# Annualized standard deviation of daily returns
backtest.std

# Sharpe ratio (using 3 month T-Bill as risk free asset)
backtest.sharpe

# Sortino ratio (using 3 month T-Bill as risk free asset)
backtest.sortino

# Pearson correlation coefficient with the S&P 500
backtest.correlation

# Returns a pandas.Series object containing rolling returns of the specified interval (e.g. 1 year)
backtest.get_rolling_returns(12)
```


#### Graphing backtests

```python
allocation_2 = {
    'Total US Stock Market': 0.60,
    'Total Intl Stock Market': 0.20,
    'Total US Bond Market': 0.20
}

backtest_2 = tsf.Backtest(allocation_2, rebalance='q', name='Three Fund Portfolio')
tsf.graph_return(backtest_1, backtest_2, start_val=1000, logarithmic=True, path='returns.png')
tsf.graph_drawdown(backtest_1, backtest_2, path='drawdowns.png')
tsf.graph_rolling_returns(backtest_1, backtest_2, interval=24, path='rolling_returns.png')
```

#### Output
![returns](https://github.com/BradleyHe/testfolio/raw/main/example/returns.png)
![drawdowns](https://github.com/BradleyHe/testfolio/raw/main/example/drawdowns.png)
![rolling_returns](https://github.com/BradleyHe/testfolio/raw/main/example/rolling_returns.png)

