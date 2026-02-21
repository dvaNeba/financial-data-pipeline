def analyze(df):
    stats = {
        "mean_price": df["Close"].mean(),
        "volatility": df["Daily_Return"].std(),
        "max_price": df["Close"].max(),
        "min_price": df["Close"].min()
    }

    print("Basic Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    return stats

