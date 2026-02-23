import logging
import argparse
from datetime import datetime, timedelta

from config import *
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


def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Invalid date format: {date_str}. Use YYYY-MM-DD."
        )


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Financial Data Pipeline CLI"
    )

    parser.add_argument(
        "--ticker",
        type=str,
        default=DEFAULT_TICKER,
        help="Stock ticker symbol (e.g., AAPL)"
    )

    parser.add_argument(
        "--start",
        type=validate_date,
        default=None,
        help="Optional start date override (YYYY-MM-DD)"
    )

    parser.add_argument(
        "--end",
        type=validate_date,
        default=None,
        help="Optional end date override (YYYY-MM-DD)"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    ticker = args.ticker
    today = args.end if args.end else datetime.today().strftime("%Y-%m-%d")

    max_date = get_max_date(DB_CONFIG, ticker)

    if args.start:
        start_date = args.start
    else:
        start_date = (
            (max_date + timedelta(days=1)).strftime("%Y-%m-%d")
            if max_date else DEFAULT_START_DATE
        )

    if start_date >= today:
        logging.info("Database already contains the latest available data.")
    else:
        logging.info(f"Fetching data for {ticker} from {start_date} to {today}")
        df = fetch_stock_data(ticker, start_date, today)

        if df.empty:
            logging.info("No new data available.")
        else:
            df_clean = clean_data(df)
            save_to_postgres(df_clean, DB_CONFIG, ticker)
            logging.info("New data inserted successfully.")

    full_df = load_full_data(DB_CONFIG, ticker)

    if full_df.empty:
        logging.warning("No data available in the database to visualize.")
        return

    full_df = convert_date(full_df)
    full_df = calculate_ma(full_df)

    stats = analyze(full_df)
    visualize(full_df)


if __name__ == "__main__":
    main()
