import pandas as pd
import ta
import os

# Ensure processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Load processed data
df = pd.read_csv("data/processed/BTCUSDT_clean.csv")

# --- 1. Returns ---
df["return_1d"] = df["close"].pct_change()
df["return_7d"] = df["close"].pct_change(7)

# --- 2. Rolling Volatility ---
df["volatility_7d"] = df["close"].rolling(7).std()

# --- 3. Technical Indicators ---
df["rsi"] = ta.momentum.RSIIndicator(df["close"]).rsi()
df["sma_20"] = df["close"].rolling(20).mean()
df["sma_50"] = df["close"].rolling(50).mean()
df["sma_200"] = df["close"].rolling(200).mean()
df["macd"] = ta.trend.MACD(df["close"]).macd()

# Optional: drop rows with NaN (first few rows due to rolling windows)
df = df.dropna()

# --- 4. Save feature-engineered data ---
df.to_csv("data/processed/BTCUSDT_features.csv", index=False)
print("Feature-engineered data saved to data/processed/BTCUSDT_features.csv")
