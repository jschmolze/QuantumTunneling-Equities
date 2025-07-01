from Analysis import analyze_stock, plot_price_vs_potential, plot_rolling_correlation
from Data import get_random_sp500_tickers

def main():
    tickers = get_random_sp500_tickers()
    print("Analyzing tickers:", tickers)
    
    for t in tickers:
        try:
            df = analyze_stock(t)
            plot_price_vs_potential(df, t)
            plot_rolling_correlation(df, t)
        except Exception as e:
            print(f"Error analyzing {t}: {e}")

if __name__ == "__main__":
    main()
