import pandas as pd
import logging

from sqlalchemy import create_engine, text
from datetime import timedelta


def get_max_date(db_config, ticker):
    connection_string = (
        f"postgresql://{db_config['user']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )

    engine = create_engine(connection_string)

    query = text("""
        SELECT MAX(date)
        FROM analytics.stock_prices
        WHERE ticker = :ticker
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"ticker": ticker}).scalar()

    return result



def save_to_postgres(df, db_config, ticker):
    connection_string = (
        f"postgresql://{db_config['user']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )

    engine = create_engine(connection_string)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df.reset_index()
    df["ticker"] = ticker

    df = df.rename(columns={
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume",
        "Daily_Return": "daily_return",
    })

    df = df[[
        "ticker", "date", "open", "high", "low",
        "close", "volume", "daily_return"
    ]]

    insert_query = text("""
        INSERT INTO analytics.stock_prices
        (ticker, date, open, high, low, close, volume,
         daily_return)
        VALUES
        (:ticker, :date, :open, :high, :low, :close,
         :volume, :daily_return)
        ON CONFLICT (ticker, date) DO NOTHING
    """)

    with engine.begin() as conn:
        conn.execute(insert_query, df.to_dict(orient="records"))

    logging.info("Incremental insert completed.")


def load_full_data(db_config, ticker):
    connection_string = (
        f"postgresql://{db_config['user']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )

    engine = create_engine(connection_string)

    query = """
        SELECT *
        FROM analytics.stock_prices
        WHERE ticker = %(ticker)s
        ORDER BY date
    """

    df = pd.read_sql(query, engine, params={"ticker": ticker})

    return df

