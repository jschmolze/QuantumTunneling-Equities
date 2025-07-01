import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from MSFT_Example import data


def lead_lag_correlation(x, y, lag_back=250, lag_forward=60):
    """
    Compute correlation between x and y for lags in [-lag_back, +lag_forward]
    Returns: lags, correlations
    """
    lags = np.arange(-lag_back, lag_forward + 1)
    correlations = [x.shift(-lag).corr(y) for lag in lags]
    return lags, correlations

def plot_lead_lag(df, target_col, feature_cols, max_lag=250):
    """
    Plot lead-lag correlation for each feature vs target_col
    """
    plt.figure(figsize=(12, 6))
    for col in feature_cols:
        lags, corrs = lead_lag_correlation(df[col], df[target_col], max_lag)
        plt.plot(lags, corrs, label=f"{col} vs {target_col}")
    
    plt.axvline(0, color='black', linestyle='--', alpha=0.6)
    plt.xlabel("Lag (days)")
    plt.ylabel("Correlation")
    plt.title(f"Lead-Lag Correlation vs {target_col}")
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    feature_cols = ['V', 'volatility', 'mkt_draw', 'val_dev', 'inv_volume']
    plot_lead_lag(data, target_col='Close_msft', feature_cols=feature_cols)
    
lag_back = 250
lag_forward = 60

for col in feature_cols:
    lags, corrs = lead_lag_correlation(data[col], data['Close_msft'], lag_back, lag_forward)
    peak_idx = np.argmax(np.abs(corrs))
    peak_lag = lags[peak_idx]
    peak_corr = corrs[peak_idx]
    direction = "leads" if peak_lag < 0 else "lags" if peak_lag > 0 else "aligned"
    print(f"{col}: peak corr = {peak_corr:.3f} at lag = {peak_lag} → {col} {direction} price")
