import pandas as pd

# 1. Load clean data
brent_data = pd.read_csv("Brent_Crude_Data_CLEANED.csv", header=[0, 1], index_col=0, parse_dates=True)

# 1. Look at the first 5 rows to see what the data actually looks like
print(brent_data.head())

#Date - Self-Explanatory
#close - The final price of the oil once the market closes for the day
#Open - the exact price of one barrel of Brent crude the second the market opened for the day
#High - The absolute highest price someone paid for a barrel at any point on that day
#Low - the absolute lowest price the barrel dropped on that day
#Volume - total number of shares or contracts that successfully changed hands between buyers and sellers on that day

# 2. Get a technical summary (checks for missing values and data types)
print("\nInfo")
print(brent_data.info())

# 3. Generate summary statistics (mean, min, max for every column)
print("\nDescribe")
print(brent_data.describe())