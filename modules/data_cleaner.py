import pandas as pd

def clean_data(df):
    df = df.copy()

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df["Daily_Return"] = df["Close"].pct_change()
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()

    return df

