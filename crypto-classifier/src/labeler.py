import pandas as pd
import os

# Ensure processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Load feature-engineered data
df = pd.read_csv("data/processed/BTCUSDT_features.csv")

# Calculate future return (next day)
df["future_return"] = df["close"].pct_change().shift(-1)

# Create labels
def create_label(row):
    if row["future_return"] > 0.02:
        return 2  # BUY
    elif row["future_return"] < -0.02:
        return 0  # SELL
    else:
        return 1  # HOLD

df["label"] = df.apply(create_label, axis=1)

# Drop rows with NaN (last row due to shift)
df = df.dropna()

# Save labeled data
df.to_csv("data/processed/BTCUSDT_labeled.csv", index=False)
print("Labeled data saved to data/processed/BTCUSDT_labeled.csv")
