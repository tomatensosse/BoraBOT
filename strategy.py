import pandas as pd

def should_buy(df):
    return df['close'].iloc[-1] > df['ma'].iloc[-1]

def should_sell(df):
    return df['close'].iloc[-1] < df['ma'].iloc[-1]

def should_hold(df, threshold=0.02):
    return abs((df['close'].iloc[-1] - df['ma'].iloc[-1]) / df['ma'].iloc[-1]) <= threshold