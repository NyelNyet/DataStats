import matplotlib.pyplot as plt
import pandas as pd

# 1. Load clean data
brent_data = pd.read_csv("Brent_Crude_Data_CLEANED.csv", header=[0, 1], index_col=0, parse_dates=True)

# 2. Specify 'Close' column
plt.figure(figsize=(12, 5))
plt.plot(brent_data.index, brent_data['Close'], color='red')
plt.title('Brent Crude Oil Daily Closing Prices (2021 - Present)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()