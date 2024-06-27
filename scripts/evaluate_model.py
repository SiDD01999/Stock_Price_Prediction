import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import os


def evaluate_model(data_path, model_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(model_path), exist_ok=True)

    data = pd.read_csv(data_path, index_col='Date', parse_dates=True)

    # Features and target variable
    X = data[['SMA_50', 'SMA_200']]
    y = data['Close']

    # Load the trained model
    model = joblib.load(model_path)

    # Predict and evaluate
    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    print(f"Mean Squared Error: {mse}")

    # Plot actual vs predicted prices
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, y, label='Actual Prices')
    plt.plot(data.index, predictions, label='Predicted Prices')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Normalized Price')
    plt.title('Actual vs Predicted Stock Prices')
    plt.show()


if __name__ == "__main__":
    evaluate_model('../data/processed/AAPL_preprocessed.csv', '../models/random_forest_model.joblib')
