from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(data):
    # Ensure 'net_worth' column is present
    if 'net_worth' not in data.columns:
        raise ValueError("Required column 'net_worth' is missing.")
    
    # Select all feature columns after one-hot encoding
    feature_columns = [col for col in data.columns if col != 'net_worth']
    
    X = data[feature_columns]
    y = data['net_worth']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model, X_test, y_test
