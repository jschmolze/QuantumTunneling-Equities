import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------
# 1. Define time window and fetch data
# --------------------------------------
start_date = "2018-01-01"
end_date = "2024-12-31"

msft = yf.download("MSFT", start=start_date, end=end_date)[['Close', 'Volume']].copy()
msft.columns = ['Close_msft', 'Volume']

spy = yf.download("SPY", start=start_date, end=end_date)[['Close']].copy()
spy.columns = ['Close_spy']

data = msft.join(spy, how='inner')

# --------------------------------------
# 2. Derived features for potential function
# --------------------------------------
data['log_ret'] = np.log(data['Close_msft']).diff()
data['volatility'] = data['log_ret'].rolling(window=21, min_periods=15).std()
data['spy_ma200'] = data['Close_spy'].rolling(window=200, min_periods=150).mean()
data['mkt_draw'] = (data['Close_spy'] - data['spy_ma200']).abs() / data['spy_ma200']
data['inv_volume'] = (1 / data['Volume']).rolling(21).mean()
data['p_dcf_rolling'] = data['Close_msft'].rolling(window=250, min_periods=200).mean()
data['val_dev'] = ((data['Close_msft'] / data['p_dcf_rolling']) - 1) ** 2
data = data.dropna()

# --------------------------------------
# 3. Compute V(t)
# --------------------------------------
alpha, beta, gamma, delta = 1.0, 1.0, 1.0, 1.0
data['V'] = (
    alpha * data['volatility'] ** 2 +
    beta * data['mkt_draw'] +
    gamma * data['val_dev'] +
    delta * data['inv_volume']
)

# --------------------------------------
# 4. Plot V(t) vs MSFT Price
# --------------------------------------
fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.set_title("MSFT Potential Function V(t) vs Price", fontsize=16)
ax1.set_xlabel("Date")
ax1.set_ylabel("Potential V(t)", color='red')
ax1.plot(data.index, data['V'], color='red', linewidth=1.8)
ax1.tick_params(axis='y', labelcolor='red')
ax2 = ax1.twinx()
ax2.set_ylabel("MSFT Price", color='blue')
ax2.plot(data.index, data['Close_msft'], color='blue', alpha=0.6)
ax2.tick_params(axis='y', labelcolor='blue')
fig.tight_layout()
plt.grid(True)
plt.show()

# --------------------------------------
# 5. Rolling Correlations — Each Component vs Price
# --------------------------------------
corrs = pd.DataFrame(index=data.index)
corrs['volatility^2'] = data['Close_msft'].rolling(60).corr(data['volatility'] ** 2)
corrs['market_drawdown'] = data['Close_msft'].rolling(60).corr(data['mkt_draw'])
corrs['valuation_deviation'] = data['Close_msft'].rolling(60).corr(data['val_dev'])
corrs['inverse_liquidity'] = data['Close_msft'].rolling(60).corr(data['inv_volume'])

# --------------------------------------
# 6. Plot Correlation Decomposition
# --------------------------------------
plt.figure(figsize=(15, 7))
for col in corrs.columns:
    plt.plot(corrs.index, corrs[col], label=col, linewidth=1.5)

plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.title("60-Day Rolling Correlations with MSFT Price")
plt.xlabel("Date")
plt.ylabel("Correlation Coefficient")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Compute 60-day rolling correlation between MSFT price and potential V(t)
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



