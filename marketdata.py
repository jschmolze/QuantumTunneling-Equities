"""
market_data.py

Fetches real-time 10-Year Treasury yield from FRED.
Falls back to default if data unavailable.
"""

import os
from fredapi import Fred
from constants import RISK_FREE_RATE

def get_10yr_treasury_yield():
    """
    Gets most recent 10-Year Treasury yield from FRED.
    Returns decimal form (e.g., 0.042 for 4.2%).

    Falls back to RISK_FREE_RATE if fetch fails.

    Returns:
        float: Risk-free rate
    """
    try:
        api_key = os.getenv("FRED_API_KEY")
        if not api_key:
            raise EnvironmentError("FRED_API_KEY not found in environment variables.")

        fred = Fred(api_key=api_key)
        series = fred.get_series_latest_release("DGS10")
        latest_value = series.dropna().iloc[-1]

        return float(latest_value) / 100  # Convert from percent to decimal
    except Exception as e:
        print(f"[WARN] Failed to fetch 10Y yield. Using fallback. Error: {e}")
        return RISK_FREE_RATE
