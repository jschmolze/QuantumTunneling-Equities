# Quantum Tunneling in Equity Markets: MSFT Potential Function Decomposition

This repository contains the first empirical test of a quantum tunneling-inspired financial model applied to Microsoft (MSFT). The core idea is to model price movements as tunneling behavior through a dynamic potential well, where market conditions define the shape of the potential landscape.

## 🔍 Project Overview

We define a time-varying potential function \( V(t) \) composed of four interpretable market signals:

- **Volatility Squared** (\( \sigma_t^2 \)) — resistance due to realized risk
- **Market Drawdown** (\( D_t \)) — deviation of SPY from its long-term trend
- **Valuation Deviation** (\( \Delta_t^2 \)) — squared distance from a dynamic DCF anchor
- **Inverse Liquidity** (\( 1 / \text{Volume}_t \)) — proxy for frictions in execution

Each term is computed using rolling windows (21–250 days), and all components are standardized into a composite potential function:
\[
V(t) = \alpha \cdot \sigma_t^2 + \beta \cdot D_t + \gamma \cdot \Delta_t^2 + \delta \cdot \left(\frac{1}{\text{Volume}_t}\right)
\]

## 🧪 Recent Progress

- **Correlation Decomposition:**  
  We ran 60-day rolling correlations between each component and MSFT price. Volatility and market drawdown show consistent structural alignment with price behavior. Inverse liquidity was found to be negligible in effect.

- **Valuation Term Correction:**  
  The original DCF anchor was constant over time, leading to frozen or degenerate correlation structure. We replaced this with a **250-day rolling average** of MSFT price to act as a dynamic valuation baseline. This change revealed nontrivial positive correlation between valuation deviation and price — particularly during trend breakouts.

- **Composite Correlation:**  
  Surprisingly, the full potential function \( V(t) \) exhibited strong *positive* correlation with MSFT price, suggesting that rising "resistance" coincides with directional momentum — a challenge to the original barrier-suppression intuition and an opening toward viewing \( V(t) \) as latent energy.

## Figures and Output

See the `figures/` directory or Overleaf white paper for:
- Component-wise correlation plots
- Updated potential function behavior
- Visual comparison of constant vs rolling DCF models

## Next Steps

1. **Lead–Lag Testing** to determine if \( V(t) \) has predictive value for future returns  
2. **Granger Causality Analysis** across components  
3. **Weight Optimization** for \( \alpha, \beta, \gamma, \delta \) via regression  
4. **Cross-Asset Validation** on other large-cap equities or sectors

## 🛠 Code Structure

- `MSFT_Test` — Folder that features the main code for the MSFT example test
- `whitepaper` — Folder that has white papers summarizing total progress for each task

