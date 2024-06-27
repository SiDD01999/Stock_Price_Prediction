# Stock Price Prediction Project

This project aims to develop a predictive model for forecasting stock prices using historical data. The project includes data collection, preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment.


## Project Overview

This project uses historical stock data to predict future stock prices. The workflow includes:

1. **Data Collection**: Downloading historical stock data using the `yfinance` library.
2. **Data Preprocessing**: Cleaning and preparing the data for modeling.
3. **Exploratory Data Analysis (EDA)**: Analyzing the data to uncover patterns and insights.
4. **Feature Engineering**: Creating additional features to improve model performance.
5. **Model Training**: Training a machine learning model to predict stock prices.
6. **Model Evaluation**: Evaluating the performance of the model.
7. **Deployment**: Deploying the model to make predictions on new data.

## Prerequisites

- Python 3.7+
- Required Python libraries:
  - yfinance
  - pandas
  - scikit-learn
  - joblib
  - matplotlib

You can install the required libraries using the following command:
```bash
    pip install -r requirements.txt
```

# Setup
## Clone the repository:

    git clone https://github.com/yourusername/Stock_Price_Prediction.git

## Navigate into project directory
    cd Stock_Price_Prediction

# Create and activate a virtual environment:

    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

## Install the required packages:


    pip install -r requirements.txt

## Running the Project
To run the entire workflow, execute the run_all.py script. This will sequentially run all the steps from data downloading to model evaluation.


    python run_all.py
## Individual Scripts
If you prefer to run each step individually, here are the commands:

### Download Data:

    python scripts/download_data.py

\### Preprocess Data:

    python scripts/preprocess_data.py

### Train Model:

    python scripts/train_model.py

### Evaluate Model:

    python scripts/evaluate_model.py

# Project Components
## Data Collection
The download_data.py script uses the yfinance library to download historical stock data. The data is saved in the data/raw directory.

## Data Preprocessing
The preprocess_data.py script handles data cleaning, feature engineering (e.g., calculating moving averages), and normalization. The processed data is saved in the data/processed directory.

## Exploratory Data Analysis (EDA)
The EDA.ipynb notebook contains code for exploratory data analysis. It includes visualizations and analysis to understand the data better.

## Model Training
The train_model.py script trains a Random Forest model using the processed data. The trained model is saved in the models directory.

## Model Evaluation
The evaluate_model.py script evaluates the trained model using Mean Squared Error (MSE) and generates plots to compare the actual and predicted stock prices.

# Results
The results of the model evaluation, including visualizations and metrics, are saved in the results directory.

# Conclusion
This project demonstrates a complete workflow for predicting stock prices using historical data. The modular structure allows for easy updates and extensions.

# Future Work
1. Explore additional features and models to improve prediction accuracy.
2. Implement real-time data fetching and prediction.
3. Create a web interface for user-friendly interaction with the model.

# Acknowledgments
This project uses the yfinance library to fetch historical stock data.# Stock_Price_Prediction
