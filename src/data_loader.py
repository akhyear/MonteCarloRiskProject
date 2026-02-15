import numpy as np
import pandas as pd
import yfinance as yf


def load_ticker_data(ticker = "SPY", start="2014-01-01", end=None):
    """
    Download ticker adjusted close prices.
    Returns cleaned price dataframe.
    """
    data = yf.download(ticker = ticker, start=start, end=end, auto_adjust=False)
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


def load_ticker_returns(ticker = "SPY", start="2014-01-01", end=None):
    """
    Convenience function:
    Download Ticker and directly return log returns.
    """
    data = load_ticker_data(ticker, start, end)
    returns = compute_log_returns(data)
    return returns