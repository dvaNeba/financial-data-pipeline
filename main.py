import logging
import os
import pandas as pd

from config import *
from datetime import datetime, timedelta

from modules.data_fetcher import fetch_stock_data
from modules.data_cleaner import clean_data
from modules.database import get_max_date, save_to_postgres, load_full_data
from modules.analyzer import analyze
from modules.analytics import calculate_ma, convert_date
from modules.visualizer import visualize

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    today = datetime.today().strftime("%Y-%m-%d")
    max_date = get_max_date(DB_CONFIG, TICKER)

    start_date = (max_date + timedelta(days=1)).strftime("%Y-%m-%d") if max_date else START_DATE

    if start_date >= today:
        logging.info("Database already contains the latest available data.")
    else:
        logging.info(f"Fetching data from {start_date} to {today}")
        df = fetch_stock_data(TICKER, start_date, today)

        if df.empty:
            logging.info("No new data available.")
        else:
            df_clean = clean_data(df)
            save_to_postgres(df_clean, DB_CONFIG, TICKER)
            logging.info("New data inserted successfully.")

    full_df = load_full_data(DB_CONFIG, TICKER)

    if full_df.empty:
        logging.warning("No data available in the database to visualize.")
        return

    # Ensure date column is datetime
    full_df = convert_date(full_df)  # from analytics.py

    # Calculate derived metrics (MA, etc.)
    full_df = calculate_ma(full_df)  # from analytics.py

    # Run analytics summary (analyzer.py)
    stats = analyze(full_df)

    # Visualize the full dataset
    visualize(full_df)

if __name__ == "__main__":
    main()
