import pandas as pd
import os

# Create folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Load raw data
df = pd.read_csv("data/raw/BTCUSDT.csv")

# Convert open_time to datetime
df["open_time"] = pd.to_datetime(df["open_time"])

# Convert numeric columns to float
for col in ["open", "high", "low", "close", "volume"]:
    df[col] = df[col].astype(float)

# Drop unused columns
df = df.drop(columns=["close_time","quote_asset_volume","num_trades","taker_base_volume","taker_quote_volume","ignore"])

# Save processed data
df.to_csv("data/processed/BTCUSDT_clean.csv", index=False)
print("Processed data saved to data/processed/BTCUSDT_clean.csv")
