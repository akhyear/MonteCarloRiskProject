

import numpy as np


def var_violations(returns, var_series):
    """
    Count VaR violations.
    """
    violations = returns < var_series
    return violations.sum(), violations.mean()


def kupiec_test(returns, var_series, alpha=0.05):
    """
    Kupiec Proportion of Failures Test
    """
    T = len(returns)
    failures = (returns < var_series).sum()
    p_hat = failures / T

    # Likelihood ratio statistic
    LR = -2 * (
        np.log(((1 - alpha) ** (T - failures) * alpha ** failures)) -
        np.log(((1 - p_hat) ** (T - failures) * p_hat ** failures))
    )

    return LR