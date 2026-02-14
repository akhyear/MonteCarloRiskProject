import numpy as np
from scipy import stats


# ===============================
# Normal Distribution
# ===============================

def fit_normal(returns):
    """
    Fit Normal distribution via MLE.
    Returns (mu, sigma)
    """
    mu = returns.mean()
    sigma = returns.std()
    return mu, sigma


def normal_loglikelihood(returns, mu, sigma):
    return np.sum(stats.norm.logpdf(returns, mu, sigma))


# ===============================
# Student-t Distribution
# ===============================

def fit_student_t(returns):
    """
    Fit Student-t distribution via MLE.
    Returns (nu, mu, sigma)
    """
    nu, mu, sigma = stats.t.fit(returns)
    return nu, mu, sigma


def student_t_loglikelihood(returns, nu, mu, sigma):
    return np.sum(stats.t.logpdf(returns, nu, mu, sigma))


# ===============================
# Skew-Normal Distribution
# ===============================

def fit_skew_normal(returns):
    """
    Fit Skew-Normal distribution via MLE.
    Returns (alpha, mu, sigma)
    """
    alpha, mu, sigma = stats.skewnorm.fit(returns)
    return alpha, mu, sigma


def skew_normal_loglikelihood(returns, alpha, mu, sigma):
    return np.sum(stats.skewnorm.logpdf(returns, alpha, mu, sigma))