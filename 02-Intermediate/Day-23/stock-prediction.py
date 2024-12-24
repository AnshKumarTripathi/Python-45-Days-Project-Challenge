import pandas as pd
import matplotlib.pyplot as plt

def preprocess_data(file_path):
    # Step 1: Data Preprocessing
    data = pd.read_csv(file_path)
    
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Sort the data by date
    data = data.sort_values('Date')
    
    # Reset the index
    data = data.reset_index(drop=True)
    
    return data

def plot_eda(data):
    # Step 2: Exploratory Data Analysis (EDA)
    # Plotting the historical closing prices
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Closing Price')
    plt.title('Tesla Stock Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()
    
    # Descriptive statistics
    print(data.describe())

if __name__ == "__main__":
    file_path = 'Python/Learning-Projects/Python-45-Days-Project-Challenge/02-Intermediate/Day-23/Tesla.csv'
    data = preprocess_data(file_path)
    plot_eda(data)
