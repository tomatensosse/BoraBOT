import ccxt
import pandas as pd
import ta.trend

import pnl
import strategy

trades = []

def execute_strategy():
    global trades

    exchange = ccxt.binance()

    symbol = 'BTC/USDT'
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1m')

    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['ma'] = ta.trend.sma_indicator(df['close'], window=14)

    if strategy.should_buy(df):
        buy_price = df['close'].iloc[-1]
        trades.append({'buy_price': buy_price, 'sell_price': None})
        print(f"Buy signal | {buy_price}")
    elif strategy.should_sell(df):
        sell_price = "nothing to sell"
        if trades and trades[-1]['sell_price'] is None:
            sell_price = df['close'].iloc[-1]
            trades[-1]['sell_price'] = sell_price
        print(f"Sell signal | {sell_price}")
    elif strategy.should_hold(df):
        print("Hold signal")
    else:
        print("No clear signal")

    if trades and trades[-1]['sell_price'] is not None:  #Calculate profit and loss only if a trade has been closed
        total_pnl = pnl.calculate_pnl(trades)
        pnl.save_pnl(total_pnl)
        print(f"Total PnL: {total_pnl}")

def debug():
    trades = [
        {'buy_price': 100, 'sell_price': 110},
        {'buy_price': 90, 'sell_price': 85}]

    total_pnl = pnl.calculate_pnl(trades)
    pnl.save_pnl(total_pnl)
    print(f"Total PnL: {total_pnl}")