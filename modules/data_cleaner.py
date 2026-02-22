import pandas as pd

def clean_data(df):
    df = df.copy()

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df["Daily_Return"] = df["Close"].pct_change()

    return df

