import logging
import os

from config import *
from modules.data_fetcher import fetch_stock_data
from modules.data_cleaner import clean_data
from modules.analyzer import analyze
from modules.visualizer import visualize

logging.basicConfig(level=logging.INFO)

def main():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)

    df = fetch_stock_data(TICKER, START_DATE, END_DATE)
    df.to_csv(RAW_DATA_PATH)

    df_clean = clean_data(df)
    df_clean.to_csv(PROCESSED_DATA_PATH)

    analyze(df_clean)
    visualize(df_clean)

if __name__ == "__main__":
    main()

