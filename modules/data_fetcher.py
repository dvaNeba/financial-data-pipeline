import yfinance as yf
import logging

def fetch_stock_data(ticker, start, end):
    try:
        logging.info(f"Fetching data for {ticker}")
        df = yf.download(ticker, start=start, end=end)
        logging.info("Data fetched successfully")
        return df
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        raise

