I worked on this project as an introduction to fintech. The goal was to build an ETL pipeline that would fetch hourly Yahoo Finance data (Open, High, Low, Close and Volume values) for different tickers and save them in CSV files, sorted by date and without any duplicates. 
This repo contains 
  the Python script etl.py that fetches the data,
  utils.py that contains the functions, such as save_as_CSV, used in the main script,
  config.py that contains the list of tickers and path to store the resulting CSV files, 
  the bash script run_etl.sh that runs the etl.py and 
  some example resulting CSV files of this pipeline. 
Cron can be used to run the bash script everyday at a set time.
