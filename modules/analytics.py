# modules/analytics.py

import pandas as pd

def calculate_ma(df: pd.DataFrame, windows=[20, 50]) -> pd.DataFrame:
    """
    Calculate moving averages on full dataset.
    df: must contain 'close' column.
    """
    df = df.copy()
    for w in windows:
        df[f"ma_{w}"] = df["close"].rolling(window=w).mean()
    return df

def convert_date(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure date column is datetime type.
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    return df

