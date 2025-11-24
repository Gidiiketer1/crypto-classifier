import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Ensure processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Load labeled data
df = pd.read_csv("data/processed/BTCUSDT_labeled.csv")

# Features and target
X = df.drop(columns=["label", "open_time", "future_return"])
y = df["label"]

# First split: Train vs Temp (70% train, 30% temp)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, shuffle=False
)

# Second split: Validation vs Test (50% each of temp → 15% each of total)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, shuffle=False
)

# Save splits as CSV (optional, for inspection)
os.makedirs("data/splits", exist_ok=True)
X_train.to_csv("data/splits/X_train.csv", index=False)
X_val.to_csv("data/splits/X_val.csv", index=False)
X_test.to_csv("data/splits/X_test.csv", index=False)
y_train.to_csv("data/splits/y_train.csv", index=False)
y_val.to_csv("data/splits/y_val.csv", index=False)
y_test.to_csv("data/splits/y_test.csv", index=False)

print("Train, validation, and test splits created in data/splits/")
print("Shapes:", X_train.shape, X_val.shape, X_test.shape)
