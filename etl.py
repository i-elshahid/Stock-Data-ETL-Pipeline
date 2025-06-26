import yfinance as yf
import pandas as pd
from datetime import datetime
from config import TICKERS, DATA_PATH
from utils import save_to_csv, setup_logger

logger  = setup_logger("logs/etl.log")

def fetch_data(ticker):
    try:
        df = yf.download(ticker, period="100d", interval="1h") #changes the period of time for 
        #which the data is fetched
        #interval is time between each data point
        if not df.empty:
            df.reset_index(inplace=True)
            save_to_csv(df, ticker, DATA_PATH)
            logger.info(f"Fetched data for {ticker}")
        else:
            logger.warning(f"No data for {ticker}")
    except Exception as e:
        logger.error(f"Error fetching {ticker}: {str(e)}")


def main():
    for ticker in TICKERS:
        fetch_data(ticker)


if __name__=="__main__":
    main()
