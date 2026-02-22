# modules/analyzer.py

import pandas as pd

def analyze(df: pd.DataFrame) -> dict:
    """
    Calculate basic statistics using pandas display precision.
    """

    decimals = pd.get_option("display.precision")

    mean_price = round(df["close"].mean(), decimals)
    max_price = round(df["close"].max(), decimals)
    min_price = round(df["close"].min(), decimals)
    volatility = round(df["daily_return"].std(), 5)

    print("Basic Statistics:")
    print(f"mean_price: {mean_price:.{decimals}f}")
    print(f"volatility: {volatility:.5f}")
    print(f"max_price: {max_price:.{decimals}f}")
    print(f"min_price: {min_price:.{decimals}f}")

    return {
        "mean_price": mean_price,
        "volatility": volatility,
        "max_price": max_price,
        "min_price": min_price
    }
