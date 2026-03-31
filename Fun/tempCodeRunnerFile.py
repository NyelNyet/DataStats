import yfinance as yf
import pandas as pd
import os

# 1. Define the ticker for Brent Crude Oil
ticker = "BZ=F"

# 2. Download the daily historical data
print("Fetching data from Yahoo Finance...")
brent_data = yf.download(ticker, start="2021-03-15", interval="1d")

# 3. Save it directly to a CSV file
raw_file_name = "Brent_Crude_Data_2021_to_Present_RawData.csv"
cleaned_file_name = "Brent_Crude_Data_2021_to_Present_RawData.csv"

brent_data.to_csv(raw_file_name)

print(f"Success! Your data is saved as: {raw_file_name}")
print(f"Cleaning...({raw_file_name})")

brent_data = pd.read_csv(raw_file_name, index_col=0, parse_dates=True, date_format="ISO8601")

if brent_data.duplicated().sum() > 0:
    brent_data = brent_data.drop_duplicates()

if brent_data.isnull().sum().sum() > 0:
    brent_data = brent_data.ffill()

brent_data.columns = brent_data.columns.droplevel(1)

os.rename(raw_file_name, cleaned_file_name)