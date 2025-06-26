import os
import pandas as pd
import logging

def setup_logger(log_file):
    logger = logging.getLogger("etl")
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def reorder_ohlc_columns(df):
    preferred_order = ["Datetime", "Open", "High", "Low", "Close", "Volume"]
    existing_cols = df.columns.tolist()

    # Keep preferred columns in order, then add any others
    ordered_cols = [col for col in preferred_order if col in existing_cols]
    remaining_cols = [col for col in existing_cols if col not in ordered_cols]
    return df[ordered_cols + remaining_cols]



def save_to_csv(df, ticker, path):
    filename = os.path.join(path, f"{ticker}.csv")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df = reorder_ohlc_columns(df)
    if os.path.exists(filename):

        existing_df = pd.read_csv(filename)
        # Parse existing datetime too
        existing_df['Datetime'] = pd.to_datetime(existing_df['Datetime'])
        
        # Combine and remove duplicate dates
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        combined_df.drop_duplicates(subset="Datetime", inplace=True)
        combined_df.sort_values(by="Datetime", inplace=True)

        combined_df = reorder_ohlc_columns(combined_df)
        
        combined_df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, index=False)