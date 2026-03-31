import pandas as pd
import plotly.express as px

# 1. Load clean data
brent_data = pd.read_csv("Brent_Crude_Data_CLEANED.csv", index_col=0, parse_dates=True)

# 2. Calculate both Moving Averages using the clean 'Close' column
brent_data['Daily MA'] = brent_data['Close'].rolling(window=5).mean()
brent_data['Monthly MA'] = brent_data['Close'].rolling(window=21).mean()

# 3. Create the interactive plot
# Plotly is smart enough to plot all three lines at once with a list
fig = px.line(
    brent_data, 
    x=brent_data.index, 
    y=['Close', 'Daily MA', 'Monthly MA'], 
    title='Interactive Brent Crude Prices with Moving Averages (2021 - Present)',
    labels={'value': 'Price (USD)', 'Date': 'Trading Day', 'variable': 'Legend'}
)

# 4. Display the interactive graph
fig.show()