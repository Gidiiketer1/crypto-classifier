import requests
import pandas as pd
import os

# Create folders if they don't exist
os.makedirs("data/raw", exist_ok=True)

def fetch_binance(symbol="BTCUSDT", interval="1d", limit=1000):
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df.columns = [
        "open_time","open","high","low","close","volume",
        "close_time","quote_asset_volume","num_trades",
        "taker_base_volume","taker_quote_volume","ignore"
    ]

    # Convert columns
    df["open_time"] = pd.to_datetime(df["open_time"], unit='ms')
    df["close"] = df["close"].astype(float)
    df["open"] = df["open"].astype(float)
    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["volume"] = df["volume"].astype(float)

    return df

# Fetch BTCUSDT data
df = fetch_binance(symbol="BTCUSDT", interval="1d", limit=1000)

# Save as CSV
df.to_csv("data/raw/BTCUSDT.csv", index=False)
print("Raw data saved to data/raw/BTCUSDT.csv")
