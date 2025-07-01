import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Data import fetch_stock_data, compute_potential, get_random_sp500_tickers

def analyze_stock(ticker, start_date="2018-01-01", end_date="2024-12-31", 
                  alpha=1.0, beta=1.0, gamma=1.0, delta=1.0):
    data = fetch_stock_data(ticker, start_date, end_date)
    data = compute_potential(data, alpha, beta, gamma, delta)
    data.rename(columns={'Close': f'Close_{ticker}'}, inplace=True)
    return data


def plot_price_vs_potential(data, ticker):
    fig, ax1 = plt.subplots(figsize=(14, 6))
    ax1.set_title(f"{ticker} Potential Function V(t) vs Price", fontsize=16)
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Potential V(t)", color='red')
    ax1.plot(data.index, data['V'], color='red', linewidth=1.8)
    ax1.tick_params(axis='y', labelcolor='red')
    ax2 = ax1.twinx()
    ax2.set_ylabel(f"{ticker} Price", color='blue')
    ax2.plot(data.index, data[f'Close_{ticker}'], color='blue', alpha=0.6)
    ax2.tick_params(axis='y', labelcolor='blue')
    fig.tight_layout()
    plt.grid(True)
    plt.show()

def plot_rolling_correlation(data, ticker):
    data['rolling_corr'] = data[f'Close_{ticker}'].rolling(window=60).corr(data['V'])
    plt.figure(figsize=(14, 5))
    plt.plot(data.index, data['rolling_corr'], label='60-day Rolling Correlation', color='purple')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.title(f"Rolling 60-Day Correlation Between {ticker} Price and Potential V(t)")
    plt.xlabel("Date")
    plt.ylabel("Correlation Coefficient")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()