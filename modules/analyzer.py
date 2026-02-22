def analyze(df):
    stats = {
        "mean_price": df["close"].mean(),
        "volatility": df["daily_return"].std(),
        "max_price": df["close"].max(),
        "min_price": df["close"].min()
    }

    print("Basic Statistics:")
    for key, value in stats.items():
        print(f"{key}: {value}")

    return stats

