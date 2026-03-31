import yfinance as yf
import pandas as pd

# 1. Define the ticker
ticker = "BZ=F"

# 2. Download the raw data
print("Fetching data from Yahoo Finance...")
brent_data = yf.download(ticker, start="2021-03-15", interval="1d")

# 3. SAVE #1: Save the exact, untouched raw data
raw_file = "Brent_Crude_Data_RAW.csv"
brent_data.to_csv(raw_file)
print(f"-> Raw data saved as: {raw_file}")

# 4. Clean the data in memory
print("Cleaning data...")
brent_data.columns = brent_data.columns.droplevel(1) # Drop 'BZ=F'

if brent_data.duplicated().sum() > 0:
    brent_data = brent_data.drop_duplicates()

if brent_data.isnull().sum().sum() > 0:
    brent_data = brent_data.ffill()

# 5. SAVE #2: Save the perfectly clean data
clean_file = "Brent_Crude_Data_CLEANED.csv"
brent_data.to_csv(clean_file)
print(f"-> Clean data saved as: {clean_file}")

print("Pipeline complete! Both files are ready in your folder.")