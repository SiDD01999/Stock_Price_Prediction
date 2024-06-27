import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os


def preprocess_data(file_path, save_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)

    # Create features: moving averages
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Close'].rolling(window=200).mean()

    # Drop rows with NaN values
    data = data.dropna()

    # Normalize the features
    scaler = MinMaxScaler()
    data[['Close', 'SMA_50', 'SMA_200']] = scaler.fit_transform(data[['Close', 'SMA_50', 'SMA_200']])

    data.to_csv(save_path)
    print(f"Data preprocessed and saved to {save_path}")


if __name__ == "__main__":
    preprocess_data('../data/raw/AAPL.csv', '../data/processed/AAPL_preprocessed.csv')
