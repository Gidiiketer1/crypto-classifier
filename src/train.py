import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load processed train/validation data
X_train = pd.read_csv("data/splits/X_train.csv")
y_train = pd.read_csv("data/splits/y_train.csv").squeeze()
X_val = pd.read_csv("data/splits/X_val.csv")
y_val = pd.read_csv("data/splits/y_val.csv").squeeze()

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Initialize XGBoost classifier
model = XGBClassifier(
    max_depth=5,
    n_estimators=200,
    learning_rate=0.1,
    eval_metric="mlogloss",
    use_label_encoder=False
)

# Train the model
model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=True)

# Evaluate on validation set
y_val_pred = model.predict(X_val)
print("Validation Classification Report:\n")
print(classification_report(y_val, y_val_pred))

# Save the trained model
joblib.dump(model, "models/buy_sell_classifier.pkl")
print("Model saved to models/buy_sell_classifier.pkl")
