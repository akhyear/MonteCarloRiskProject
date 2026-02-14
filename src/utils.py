

import numpy as np


def compute_log_returns(prices):
    """
    Compute log returns from price series.
    """
    return np.log(prices / prices.shift(1)).dropna()


def summary_stats(returns):
    """
    Basic statistics for returns.
    """
    return {
        "mean": returns.mean(),
        "std": returns.std(),
        "skew": returns.skew(),
        "kurtosis": returns.kurtosis()
    }