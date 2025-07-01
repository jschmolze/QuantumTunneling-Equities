import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset created in MSFT Example.py
from MSFT_Example import data  
if __name__ == "__main__":
# Compute 60-day rolling correlations with MSFT price
    corrs = pd.DataFrame(index=data.index)
    corrs['volatility^2'] = data['Close_msft'].rolling(60).corr(data['volatility'] ** 2)
    corrs['market_drawdown'] = data['Close_msft'].rolling(60).corr(data['mkt_draw'])
    corrs['valuation_deviation'] = data['Close_msft'].rolling(60).corr(data['val_dev'])
    corrs['inverse_liquidity'] = data['Close_msft'].rolling(60).corr(data['inv_volume'])

    # Plot each rolling correlation on the same graph
    plt.figure(figsize=(15, 7))
    #plt.plot(corrs.index, corrs['volatility^2'], label='Volatility²', linewidth=1.5)
    #plt.plot(corrs.index, corrs['market_drawdown'], label='Market Drawdown', linewidth=1.5)
    #plt.plot(corrs.index, corrs['valuation_deviation'], label='Valuation Deviation', linewidth=1.5)
    #plt.plot(corrs.index, corrs['inverse_liquidity'], label='Inverse Liquidity', linewidth=1.5)

    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.title("Rolling 60-Day Correlations Between MSFT Price and Components of V(t)", fontsize=15)
    plt.xlabel("Date")
    plt.ylabel("Correlation Coefficient")
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
