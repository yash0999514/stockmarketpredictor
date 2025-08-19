import numpy as np

def plot_stock_data(data, fig, canvas):
    fig.clear()
    ax = fig.add_subplot(111)
    ax.plot(data['Close'], label='Closing Price', color='blue')
    ax.set_title("Historical Stock Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    canvas.draw()

def predict_stock(data, label):
    last_5 = data['Close'].tail(5)
    predicted = round(last_5.mean(), 2)
    label.config(text=f"Predicted next close price (avg of last 5 days): ₹{predicted}")
def show_risk_return(data, label):
    import numpy as np
    from datetime import datetime, timedelta
    import pandas as pd

    # Use last 30 rows of data
    last_30 = data.tail(30)

    # Safety checks
    if len(last_30) < 2 or 'Close' not in last_30.columns:
        label.config(text="Not enough data for risk-return analysis.")
        return

    try:
        # Force Close to be a 1D float Series (not a DataFrame)
        close = last_30['Close']
        if isinstance(close, pd.DataFrame):
            close = close.iloc[:, 0]

        # Extract float values safely
        start_price = float(close.iloc[0])
        end_price = float(close.iloc[-1])
        change_pct = ((end_price - start_price) / start_price) * 100

        daily_returns = close.pct_change().dropna()
        volatility = float(daily_returns.std()) * 100

        result_text = (
            f"Risk-Return (Last 30 Days)\n"
            f"Start Price: ₹{start_price:.2f}\n"
            f"End Price: ₹{end_price:.2f}\n"
            f"Change: {change_pct:+.2f}%\n"
            f"Volatility: {volatility:.2f}%"
        )

        label.config(text=result_text)

    except Exception as e:
        label.config(text=f"Error: {str(e)}")



