# Quantum Tunneling in Equity Markets: MSFT Potential Function Decomposition

This repository contains the first empirical test of a quantum tunneling-inspired financial model applied to Microsoft (MSFT). The core idea is to model price movements as tunneling behavior through a dynamic potential well, where market conditions define the shape of the potential landscape.

## Project Overview

We define a time-varying potential function `V(t)` composed of four interpretable market signals:

- **Volatility Squared** (`σ²ₜ`) — resistance due to realized risk  
- **Market Drawdown** (`Dₜ`) — deviation of SPY from its long-term trend  
- **Valuation Deviation** (`Δ²ₜ`) — squared distance from a dynamic DCF anchor  
- **Inverse Liquidity** (`1 / Volumeₜ`) — proxy for frictions in execution  

Each term is computed using rolling windows (21–250 days), and all components are combined into a composite potential function:

V(t) = α · σ²ₜ + β · Dₜ + γ · Δ²ₜ + δ · (1 / Volumeₜ)


## Recent Progress

- **Correlation Decomposition:**  
  We computed 60-day rolling correlations between each component and MSFT price. Volatility and market drawdown show consistent alignment with price behavior. Inverse liquidity was found to be statistically weak and may be dropped.

- **Valuation Term Correction:**  
  The original model used a constant DCF anchor, which caused the valuation deviation term to behave poorly in trending markets. We replaced this with a 250-day rolling average of MSFT price to act as a dynamic anchor. This significantly improved correlation structure and revealed positive alignment between valuation deviation and upward momentum.

- **Composite Correlation:**  
  Surprisingly, the full potential function `V(t)` showed strong *positive* correlation with price — suggesting that rising “resistance” may actually coincide with market energy or breakout probability.

## Next Steps

1. Lead–Lag Testing: does `V(t)` help forecast future returns?
2. Granger Causality Testing: which components cause changes in price dynamics?
3. Coefficient Optimization: refine weights `α`, `β`, `γ`, `δ` via regression
4. Out-of-Sample Validation: apply to other stocks or sectors

## Code Structure

- `MSFT_Test/` — Contains the full script for the MSFT case study
- `whitepaper/` — LaTeX-based documentation summarizing progress and results

