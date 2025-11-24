import os

project = "crypto-classifier"

folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "models"
]

files = [
    "notebooks/01_fetch_data.ipynb",
    "notebooks/02_feature_engineering.ipynb",
    "notebooks/03_model_training.ipynb",
    "notebooks/04_evaluation.ipynb",
    "src/data_fetcher.py",
    "src/feature_generator.py",
    "src/labeler.py",
    "src/train.py",
    "src/predict.py",
    "README.md",
    "requirements.txt"
]

# Create folders
for folder in folders:
    os.makedirs(f"{project}/{folder}", exist_ok=True)

# Create empty files
for file in files:
    open(f"{project}/{file}", "w").close()

print("🎉 Project structure created successfully!")
