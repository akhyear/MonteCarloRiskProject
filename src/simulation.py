import numpy as np
from scipy import stats


def simulate_normal(mu, sigma, n_days=252, n_sims=10000):
    """
    Simulate returns using Normal distribution.
    """
    sims = np.random.normal(mu, sigma, size=(n_days, n_sims))
    return sims


def simulate_student_t(mu, sigma, df, n_days=252, n_sims=10000):
    """
    Simulate returns using Student-t distribution.
    """
    t_random = stats.t.rvs(df, size=(n_days, n_sims))
    
    # Scale to match desired sigma
    scaled = mu + sigma * t_random / np.sqrt(df / (df - 2))
    
    return scaled