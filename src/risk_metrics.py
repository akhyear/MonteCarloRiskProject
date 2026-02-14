import numpy as np
from scipy.stats import norm


def historical_var(returns, alpha=0.05):
    """
    Historical VaR
    """
    return np.percentile(returns, 100 * alpha)


def parametric_var(mu, sigma, alpha=0.05):
    """
    Parametric Normal VaR
    """
    return mu + sigma * norm.ppf(alpha)


def expected_shortfall(returns, alpha=0.05):
    """
    Historical Expected Shortfall
    """
    var = historical_var(returns, alpha)
    return returns[returns <= var].mean()