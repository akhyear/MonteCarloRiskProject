# Kupiec Backtesting Conclusion

## Objective
The Kupiec Proportion of Failures (POF) test was applied to evaluate whether the VaR models produce the correct number of expected breaches at the chosen confidence level.

## Summary of Results

- All three models (Normal, Student-t, and Skew-Normal) were rejected at the 5% significance level.
- The observed breach rates were higher than the expected rate.
- All p-values were below 0.05, meaning the null hypothesis of correct coverage is rejected.

## Interpretation

The results indicate that:

- The **Normal distribution severely underestimates tail risk**, producing too many VaR breaches.
- The **Skew-Normal model also underestimates extreme losses**.
- The **Student-t model performs better**, but still fails to achieve statistically correct coverage.

This suggests that the return series exhibits **heavier tails and possibly volatility clustering**, which are not fully captured by these static distributional assumptions.

## Implications

- VaR estimates from these models are too optimistic.
- Risk is being underestimated.
- More advanced modeling approaches may be necessary, such as:
  - GARCH models with heavy-tailed innovations
  - Extreme Value Theory (EVT)
  - Filtered Historical Simulation

## Final Conclusion

Based on the Kupiec test results, none of the tested models provide adequate VaR coverage. The Student-t model is comparatively better but still statistically insufficient. Therefore, the current modeling framework should not be considered reliable for accurate tail risk estimation.
