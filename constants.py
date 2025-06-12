"""
constants.py

This module stores global constants used across the financial modeling system.
All constants here are fixed—no real-time market data is pulled directly in this file.
"""

# General Market Constants
RISK_FREE_RATE = 0.04        # Used as fallback if real-time yield unavailable
MARKET_RISK_PREMIUM = 0.055  # Long-run average market premium
INFLATION_TARGET = 0.02      # Central bank inflation target
EQUITY_RISK_PREMIUM = 0.05   # For CAPM-based models

# Time Conventions
TRADING_DAYS_PER_YEAR = 252
WEEKS_PER_YEAR = 52
MONTHS_PER_YEAR = 12

# Discounting & Compounding
ANNUAL_DISCOUNT_RATE = 0.08
CONTINUOUS_COMPOUNDING = True  # Toggle for pricing engines

# Valuation Multiples Benchmarks (e.g., for screening or sanity checks)
DEFAULT_P_E = 15
DEFAULT_P_B = 2
DEFAULT_EV_EBITDA = 10

# Statistical Thresholds
CONFIDENCE_LEVEL = 0.95
Z_SCORE_95 = 1.64485

# Modeling Constants
DEFAULT_BETA = 1.0
DEFAULT_LEVERAGE_RATIO = 2.0  # Debt/Equity

# Currency & Macroeconomic Assumptions
BASE_CURRENCY = "USD"
GDP_GROWTH_LONG_TERM = 0.025
TAX_RATE_CORPORATE = 0.21

# Technical Model Flags
USE_MONTE_CARLO = True
NUM_MONTE_CARLO_PATHS = 10000

# Custom Tuning Parameters
ALPHA = 0.01   # Learning rate or regularization term
LAMBDA = 0.05  # Regularization weight or penalty factor
GAMMA = 0.9    # Discount factor for dynamic models

# Placeholder constants for scenario analysis
BULL_MARKET_RETURN = 0.12
BEAR_MARKET_RETURN = -0.10
NEUTRAL_RETURN = 0.05

# Constants for financial statement modeling (if applicable)
DEPRECIATION_YEARS = 5
INVENTORY_TURNOVER_DAYS = 60
ACCOUNTS_RECEIVABLE_DAYS = 45
ACCOUNTS_PAYABLE_DAYS = 30
