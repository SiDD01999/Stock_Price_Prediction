import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os


def train_model(data_path, model_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    data = pd.read_csv(data_path, index_col='Date', parse_dates=True)

    # Features and target variable
    X = data[['SMA_50', 'SMA_200']]
    y = data['Close']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a Random Forest model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, model_path)
    print(f"Model trained and saved to {model_path}")


if __name__ == "__main__":
    train_model('../data/processed/AAPL_preprocessed.csv', '../models/random_forest_model.joblib')
