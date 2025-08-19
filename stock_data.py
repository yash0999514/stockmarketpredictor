import pandas as pd
import yfinance as yf
from tkinter import messagebox
from datetime import datetime, timedelta

# Load stock symbols
df = pd.read_csv("indian_stocks.csv")
stock_list = dict(zip(df['Symbol'], df['Company']))

def fetch_data_for_symbol(symbol):
    try:
        end = datetime.now()
        start = end - timedelta(days=365)
        data = yf.download(symbol, start=start, end=end)
        if data.empty:
            messagebox.showerror("Data Error", "No data found for this symbol.")
            return None
        data.index = pd.to_datetime(data.index)
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {str(e)}")
        return None
