import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def get_random_sp500_tickers(n=10, seed=42):
    sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    table = pd.read_html(sp500_url)
    tickers = table[0]['Symbol'].tolist()
    random.seed(seed)
    return random.sample(tickers, n)

def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.download(ticker, start=start_date, end=end_date)[['Close', 'Volume']].copy()
    stock.columns = ['Close', 'Volume']

    spy = yf.download("SPY", start=start_date, end=end_date)[['Close']].copy()
    spy.columns = ['Close_spy']

    data = stock.join(spy, how='inner')
    data['log_ret'] = np.log(data['Close']).diff()
    data['volatility'] = data['log_ret'].rolling(window=21, min_periods=15).std()
    data['spy_ma200'] = data['Close_spy'].rolling(window=200, min_periods=150).mean()
    data['mkt_draw'] = (data['Close_spy'] - data['spy_ma200']).abs() / data['spy_ma200']
    data['inv_volume'] = (1 / data['Volume']).rolling(21).mean()
    data['p_dcf_rolling'] = data['Close'].rolling(window=250, min_periods=200).mean()
    data['val_dev'] = ((data['Close'] / data['p_dcf_rolling']) - 1) ** 2
    return data.dropna()


def compute_potential(data, alpha=1.0, beta=1.0, gamma=1.0, delta=1.0):
    data = data.copy()
    data['V'] = (
        alpha * data['volatility'] ** 2 +
        beta * data['mkt_draw'] +
        gamma * data['val_dev'] +
        delta * data['inv_volume']
    )
    return data