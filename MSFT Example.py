import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------
# 1. Define time window for data
# --------------------------------------
start_date = "2018-01-01"
end_date = "2024-12-31"

# --------------------------------------
# 2. Download historical price + volume data
# --------------------------------------
msft = yf.download("MSFT", start=start_date, end=end_date)
spy = yf.download("SPY", start=start_date, end=end_date)

# --------------------------------------
# 3. Fetch EPS and compute approximate DCF valuation anchor
# --------------------------------------
ticker = yf.Ticker("MSFT")
eps_ttm = ticker.info.get('trailingEps', None)

# Fallback if EPS data is unavailable
if eps_ttm is None:
    raise ValueError("EPS (trailing twelve months) not available for MSFT.")

pe_estimate = 25  # Assumed fair-value P/E ratio
p_dcf = eps_ttm * pe_estimate  # Constant DCF-based anchor price

# --------------------------------------
# 4. Join MSFT and SPY on aligned datetime index
# --------------------------------------
# Only keep the 'Close' column from SPY and label clearly
spy = spy[['Close']].rename(columns={'Close': 'Close_spy'})
msft = msft.rename(columns={'Close': 'Close_msft'})

# Join on dates where both are available
data = msft.join(spy, how='inner')

# --------------------------------------
# 5. Compute derived features for potential function
# --------------------------------------

# 5.1 Realized Volatility (21-day rolling std dev of log returns)
data['log_ret'] = data['Close_msft'].apply(lambda x: np.log(x)).diff()
data['volatility'] = data['log_ret'].rolling(window=21, min_periods=15).std()

# 5.2 Market Drawdown (distance from 200-day MA of SPY)
data['spy_ma200'] = data['Close_spy'].rolling(window=200, min_periods=150).mean()
close_spy = data['Close_spy'].squeeze()
spy_ma200 = data['spy_ma200'].squeeze()
data['mkt_draw'] = (close_spy - spy_ma200).abs() / spy_ma200

# 5.3 Inverse Liquidity (proxy for friction)
data['inv_volume'] = 1 / data['Volume']

# 5.4 Valuation Deviation (distance from DCF anchor)
data['val_dev'] = ((data['Close_msft'] / p_dcf) - 1) ** 2

# --------------------------------------
# 6. Final cleaning — drop rows with any missing values
# --------------------------------------
data = data.dropna()

# --------------------------------------
# 7. Define potential function coefficients
# --------------------------------------
alpha = 1.0   # volatility resistance weight
beta = 1.0    # market drawdown weight
gamma = 1.0   # valuation deviation weight
delta = 1.0   # inverse liquidity weight

# --------------------------------------
# 8. Compute V(t) — total potential function
# --------------------------------------
data['V'] = (
    alpha * data['volatility'] ** 2 +
    beta * data['mkt_draw'] +
    gamma * data['val_dev'] +
    delta * data['inv_volume']
)

# Set up the plot
fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.set_title("MSFT Potential Function V(t) vs Price", fontsize=16)

# Plot V(t)
color = 'tab:red'
ax1.set_xlabel("Date")
ax1.set_ylabel("Potential V(t)", color=color)
ax1.plot(data.index, data['V'], color=color, label="Potential V(t)", linewidth=1.8)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True)

# Create second y-axis for MSFT price
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel("MSFT Price", color=color)
ax2.plot(data.index, data['Close_msft'], color=color, label="MSFT Price", alpha=0.6)
ax2.tick_params(axis='y', labelcolor=color)

# Show combined plot
fig.tight_layout()
plt.show()

data['rolling_corr'] = data['Close_msft'].rolling(window=60).corr(data['V'])

# Plot the rolling correlation
plt.figure(figsize=(14, 5))
plt.plot(data.index, data['rolling_corr'], label='60-day Rolling Correlation', color='purple')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.title("Rolling 60-Day Correlation Between MSFT Price and Potential V(t)")
plt.xlabel("Date")
plt.ylabel("Correlation Coefficient")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()



