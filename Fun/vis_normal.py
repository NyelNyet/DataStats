import matplotlib.pyplot as plt
import pandas as pd

# 1. Load clean data
brent_data = pd.read_csv("Brent_Crude_Data_CLEANED.csv", header=[0, 1], index_col=0, parse_dates=True)

# 2. Calculate both Moving Averages FIRST
brent_data['Weekly MA'] = brent_data['Close'].rolling(window=5).mean()
brent_data['Monthly MA'] = brent_data['Close'].rolling(window=21).mean()

# 3. Set up the plot size
plt.figure(figsize=(12, 5))

# 4. Plot all three lines
plt.plot(brent_data.index, brent_data['Close'], color='lightcoral', label='Daily Close', alpha=0.5)
plt.plot(brent_data.index, brent_data['Weekly MA'], color='darkred', label='Weekly Moving Average', linewidth=2)
plt.plot(brent_data.index, brent_data['Monthly MA'], color='darkblue', label='Monthly Moving Average', linewidth=2)

# 5. Add titles, labels, and the legend
plt.title('Brent Crude Oil Prices with Moving Averages (2021 - Present)', fontsize=14, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price (USD)', fontsize=12)
plt.legend()

# 6. Beautify the chart (Rotate dates, add soft grid, fix margins)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# 7. Show the final image
plt.show()