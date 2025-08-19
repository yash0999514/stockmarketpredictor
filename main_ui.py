import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from stock_data import fetch_data_for_symbol
from stock_utils import plot_stock_data, predict_stock, show_risk_return

# --- Setup Window ---
root = tk.Tk()
root.title("Stock Market: Indian NSE Prediction")
root.geometry("960x800")
root.configure(bg="#f5f6f7")

# --- Heading ---
tk.Label(root, text="Stock Market: Stock Prediction", font=("Helvetica", 20, "bold"), bg="#f5f6f7").pack(pady=(10, 5))
tk.Label(root, text="Analyze, Predict, and Manage Risks (India Only)", font=("Helvetica", 12), bg="#f5f6f7").pack(pady=(0, 15))

# --- Chart Section ---
frame_input = tk.Frame(root, bg="white", bd=2, relief="groove", padx=10, pady=10)
frame_input.pack(padx=20, pady=10, fill="x")
tk.Label(frame_input, text="Stock Data Analysis", font=("Helvetica", 14, "bold"), bg="white").pack(anchor="w")

input_frame = tk.Frame(frame_input, bg="white")
input_frame.pack(fill="x", pady=(5, 10))

entry_var = tk.StringVar()
entry = ttk.Combobox(input_frame, textvariable=entry_var, font=("Helvetica", 12))
entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

def on_typing(event):
    from stock_data import stock_list
    typed = entry_var.get().upper()
    filtered = [s for s in stock_list if s.startswith(typed)]
    entry['values'] = filtered
    if filtered:
        entry.event_generate('<Down>')

entry.bind("<KeyRelease>", on_typing)

def fetch_and_display():
    symbol = entry_var.get().upper().strip()
    if not symbol:
        messagebox.showwarning("Input Error", "Enter a valid NSE stock symbol.")
        return
    data = fetch_data_for_symbol(symbol)
    if data is not None:
        plot_stock_data(data, fig, canvas)
        predict_stock(data, prediction_label)
        show_risk_return(data, risk_label)

load_btn = ttk.Button(input_frame, text="Load Data", command=fetch_and_display)
load_btn.pack(side="right")

# --- Matplotlib Chart Area ---
frame_chart = tk.Frame(frame_input, bg="#e4e5e7", height=300)
frame_chart.pack(fill="both", expand=True)
frame_chart.pack_propagate(0)

fig = Figure(figsize=(7, 3), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=frame_chart)
canvas.get_tk_widget().pack(fill="both", expand=True)

# --- Prediction Section ---
frame_pred = tk.Frame(root, bg="white", bd=2, relief="groove", padx=10, pady=10)
frame_pred.pack(padx=20, pady=10, fill="x")

tk.Label(frame_pred, text="Stock Prediction", font=("Helvetica", 14, "bold"), bg="white").pack(anchor="w")
prediction_display = tk.Frame(frame_pred, bg="#e4e5e7", height=80)
prediction_display.pack(fill="both", expand=True)
prediction_display.pack_propagate(0)

prediction_label = tk.Label(prediction_display, text="Prediction will appear here.", font=("Helvetica", 12), bg="#e4e5e7")
prediction_label.pack(expand=True)

# --- Risk Summary Section ---
frame_risk = tk.Frame(root, bg="white", bd=2, relief="groove", padx=10, pady=10)
frame_risk.pack(padx=20, pady=10, fill="x")

tk.Label(frame_risk, text="Risk-Return Analysis + Price Summary", font=("Helvetica", 14, "bold"), bg="white").pack(anchor="w")
risk_display = tk.Frame(frame_risk, bg="#e4e5e7", height=220)
risk_display.pack(fill="both", expand=True)
risk_display.pack_propagate(0)

risk_label = tk.Label(risk_display, text="Risk-return statistics will appear here.", font=("Courier New", 10), bg="#e4e5e7", anchor="w", justify="left")
risk_label.pack(padx=10, pady=10, anchor="w")

# --- Start App ---
root.mainloop()
