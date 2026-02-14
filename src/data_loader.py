import numpy as np
import pandas as pd
import yfinance as yf


def load_spy_data(start="2014-01-01", end=None):
    """
    Download SPY adjusted close prices.
    Returns cleaned price dataframe.
    """
    data = yf.download("SPY", start=start, end=end)
    data = data.dropna()
    return data


def compute_log_returns(price_data):
    """
    Compute log returns from Adjusted Close prices.
    Returns pandas Series.
    """
    prices = price_data["Adj Close"]
    log_returns = np.log(prices / prices.shift(1))
    log_returns = log_returns.dropna()
    return log_returns


def load_spy_returns(start="2014-01-01", end=None):
    """
    Convenience function:
    Download SPY and directly return log returns.
    """
    data = load_spy_data(start, end)
    returns = compute_log_returns(data)
    return returns