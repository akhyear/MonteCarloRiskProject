# SPY Risk Modeling & Monte Carlo Simulation

This project is a simple implementation of market risk modeling using SPY (S&P 500 ETF) daily data.

The goal is to understand how different statistical assumptions affect risk estimation especially Value-at-Risk (VaR) and Expected Shortfall (ES).

Instead of building something overly complicated, this project focuses on clarity, structure, and clean implementation of core quantitative finance concepts.

---

## What This Project Covers

- Loading SPY historical price data
- Computing daily log returns
- Fitting Normal and Student-t distributions
- Monte Carlo simulation of returns
- Historical and Parametric VaR
- Expected Shortfall (ES)
- Basic VaR backtesting
- Kupiec test for model validation

---

## Why This Project?

Financial returns are not perfectly normal.  
They are skewed, heavy-tailed, and occasionally extreme.

This project compares:
- Standard Normal assumptions
- Heavy-tailed Student-t assumptions

and evaluates how they impact risk measurement.

The focus is on understanding risk behavior, not just calculating numbers.

---

## Key Concepts Implemented

- Log returns
- Distribution fitting
- Monte Carlo simulation
- Value-at-Risk (VaR)
- Expected Shortfall (ES)
- Kupiec Proportion of Failures Test

---

## How to Run

1. Install dependencies:
      - python
      - numpy
      - pandas
      - scipy
      - matplotlib
      - statsmodels 
      - yfinance
      - jupyterlab
      - seaborn
2. Load SPY data and compute returns
3. Fit distribution
4. Simulate returns
5. Compute risk metrics
6. Backtest VaR

The modules are designed to be imported into a notebook or a main script.

---

## What I Learned

- Real-world returns are heavy-tailed
- Risk models can underestimate tail risk
- Backtesting is just as important as modeling
- Clean structure matters more than clever tricks

---

## Future Improvements

- Rolling VaR
- GARCH volatility modeling
- EVT (Extreme Value Theory)
- Multi-asset portfolio risk
- Visualization dashboard

---

## Author

Built as part of my quantitative finance learning journey.

