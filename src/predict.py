import pandas as pd
import joblib
import os

# Load the trained model
model_path = "models/buy_sell_classifier.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError("Trained model not found. Run train.py first.")
model = joblib.load(model_path)

def predict(features_df):
    """
    Predict Buy(2)/Hold(1)/Sell(0) for a dataframe of features
    """
    return model.predict(features_df)

# Example usage
if __name__ == "__main__":
    # Load features (example: last 100 rows from labeled data)
    df_features = pd.read_csv("data/processed/BTCUSDT_features.csv")
    # Drop columns not used in model
    X = df_features.drop(columns=["open_time"], errors="ignore")
    
    predictions = predict(X)
    df_features["Prediction"] = predictions
    print(df_features[["open_time", "close", "Prediction"]].tail())
