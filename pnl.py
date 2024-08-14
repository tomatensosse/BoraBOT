import os

def calculate_pnl(trades):
    pnl = 0.0
    for trade in trades:
        if trade['sell_price'] is not None and trade['buy_price'] is not None:
            pnl += trade['sell_price'] - trade['buy_price']
    return pnl

def save_pnl(pnl, file_path='pnl.txt'):
    try:
        with open(file_path, 'w') as file:
            file.write(f"Total PnL: {pnl}\n")
    except Exception as e:
        print(f"Error saving PnL: {e}")

def load_pnl(file_path='pnl.txt'):
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return float(file.readline().split(": ")[1])
    except Exception as e:
        print(f"Error loading PnL: {e}")
    return 0.0