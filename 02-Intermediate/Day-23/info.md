# Stock Price Predictor

This project involves developing a model to predict Tesla stock prices using machine learning techniques. The project includes data preprocessing, feature engineering, model training, and prediction of future stock prices.

## Project Overview

1. **Data Preprocessing**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Engineering**
4. **Model Training and Prediction**
5. **Future Stock Price Prediction**

## Step 1: Data Preprocessing

**Code Explanation:**

In this step, we load the Tesla stock price dataset and preprocess it. The preprocessing includes:

- **Loading the dataset:** Reading the CSV file containing Tesla stock price data.
- **Converting the 'Date' column:** Converting the 'Date' column to datetime format for better manipulation and visualization.
- **Sorting and resetting the index:** Sorting the data by date and resetting the index to ensure chronological order.

```python
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Tesla.csv'
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'])
data = data.sort_values('Date')
data = data.reset_index(drop=True)

print(data.head())
```

## Step 2: Exploratory Data Analysis (EDA)

**Code Explanation:**

In this step, we perform exploratory data analysis (EDA) to understand the data better:

- **Plotting Historical Closing Prices:** Visualizing the closing prices over time.
- **Descriptive Statistics:** Generating statistical summaries of the dataset.

```python
plt.figure(figsize=(14, 7))
plt.plot(data['Date'], data['Close'], label='Closing Price')
plt.title('Tesla Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

print(data.describe())
```

## Step 3: Feature Engineering

**Code Explanation:**

In this step, we create new features to improve the prediction model. These features include:

- **Moving Averages (MA):** Calculating the moving averages over different windows (5, 10, 20, and 50 days).
- **Daily Returns:** Calculating the percentage change in closing prices from the previous day.
- **Bollinger Bands:** Calculating the upper, middle, and lower Bollinger Bands.
- **Exponential Moving Averages (EMA):** Calculating the 12-day and 26-day EMAs.
- **Relative Strength Index (RSI):** Calculating the RSI to measure the speed and change of price movements.

```python
df = data.copy()

df['MA_5'] = df['Close'].rolling(window=5).mean()
df['MA_10'] = df['Close'].rolling(window=10).mean()
df['MA_20'] = df['Close'].rolling(window=20).mean()
df['MA_50'] = df['Close'].rolling(window=50).mean()

df['Daily_Return'] = df['Close'].pct_change()

df['BB_Middle'] = df['MA_20']
df['BB_Upper'] = df['BB_Middle'] + 2 * df['Close'].rolling(window=20).std()
df['BB_Lower'] = df['BB_Middle'] - 2 * df['Close'].rolling(window=20).std()

df['EMA_12'] = df['Close'].ewm(span=12, adjust=False).mean()
df['EMA_26'] = df['Close'].ewm(span=26, adjust=False).mean()

window_length = 14
delta = df['Close'].diff()
gain = (delta.where(delta > 0, 0))
loss = (-delta.where(delta < 0, 0))
avg_gain = gain.rolling(window=window_length, min_periods=1).mean()
avg_loss = loss.rolling(window=window_length, min_periods=1).mean()
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

print(df.head())
```

## Step 4: Model Training and Prediction

**Code Explanation:**

In this step, we train a Random Forest Regressor model to predict stock prices using the engineered features. The steps include:

- **Splitting the data:** Dividing the data into training and testing sets.
- **Training the model:** Initializing and training the Random Forest Regressor model.
- **Evaluating the model:** Making predictions on the testing set and evaluating the model's performance using Mean Squared Error (MSE) and Mean Absolute Error (MAE).
- **Plotting actual vs. predicted prices:** Visualizing the actual and predicted stock prices.

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

df = df.dropna()

X = df[['MA_5', 'MA_10', 'MA_20', 'MA_50', 'Daily_Return', 'BB_Middle', 'BB_Upper', 'BB_Lower', 'EMA_12', 'EMA_26', 'RSI']]
y = df['Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")

plt.figure(figsize=(14, 7))
plt.plot(y_test.values, label='Actual Prices')
plt.plot(y_pred, label='Predicted Prices', linestyle='--')
plt.title('Actual vs. Predicted Stock Prices')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
```

## Step 5: Future Stock Price Prediction

**Code Explanation:**

In this step, we predict future stock prices for the next 30 days using the trained Random Forest Regressor model. The steps include:

- **Creating a future DataFrame:** Initializing a DataFrame to hold future dates and engineered features.
- **Generating future predictions:** Iteratively predicting future stock prices using the model.
- **Plotting future stock prices:** Visualizing the predicted future stock prices.

```python
future_days = 30
last_date = df['Date'].iloc[-1]
future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, future_days + 1)]
future_df = pd.DataFrame(index=future_dates, columns=X.columns)

last_values = df.iloc[-1]

for column in future_df.columns:
    if 'MA' in column or 'EMA' in column:
        window = int(column.split('_')[1])
        future_df[column] = df['Close'].rolling(window).mean().iloc[-1]
    elif 'BB' in column:
        window = 20
        std = df['Close'].rolling(window).std().iloc[-1]
        future_df['BB_Middle'] = df['MA_20'].iloc[-1]
        future_df['BB_Upper'] = df['BB_Middle'] + 2 * std
        future_df['BB_Lower'] = df['BB_Middle'] - 2 * std
    elif column == 'Daily_Return':
        future_df[column] = df['Daily_Return'].iloc[-1]
    elif column == 'RSI':
        future_df[column] = df['RSI'].iloc[-1]

future_df.ffill(inplace=True)
future_df.bfill(inplace=True)

future_predictions = model.predict(future_df)

plt.figure(figsize=(14, 7))
plt.plot(df['Date'], df['Close'], label='Historical Prices')
plt.plot(future_dates, future_predictions, label='Predicted Future Prices', linestyle='--')
plt.title('Future Stock Price Prediction')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()
```

## Alternative Model: LSTM Network

**Code Explanation:**

In this step, we implement an LSTM model to predict stock prices. The steps include:

- **Initializing the LSTM model:** Using LSTM layers to capture the time series patterns.
- **Compiling and training the model:** Training the LSTM model on the training data.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

model = Sequential()
model.add(Dense(1, input_shape=(1, X_scaled.shape[2])))
model.add(LSTM(units=50, return_sequences=True))
model.add(LSTM(units=50))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X_train, y_train, epochs=20, batch_size=1, verbose=2)

```

DISCLAIMER: This above info.md is generated by an AI assistant, not by me lamo.
