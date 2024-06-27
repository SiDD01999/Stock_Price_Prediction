import yfinance as yf
import os


def download_stock_data(ticker, start_date, end_date, save_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(save_path)
    print(f"Data downloaded and saved to {save_path}")


if __name__ == "__main__":
    download_stock_data('AAPL', '2015-01-01', '2023-01-01', '../data/raw/AAPL.csv')
