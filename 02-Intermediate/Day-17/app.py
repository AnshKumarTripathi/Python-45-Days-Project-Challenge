from flask import Flask, request, render_template
import pandas as pd
from model_selection import train_model
from feature_engineering import create_features
from data_preparation import load_data

app = Flask(__name__)

# Load data once and extract unique business categories
original_data = load_data('D:/45-Days-Challege-JS-Python/all_billionaires_1997_2024.csv')
reference_data = create_features(original_data)
business_categories = original_data['business_category'].unique()

@app.route('/')
def home():
    return render_template('index.html', business_categories=business_categories)

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form['age']
    gender = request.form['gender']
    business_category = request.form['business_category']
    
    input_data = {'age': [age], 'gender': [gender], 'business_category': [business_category]}
    data = pd.DataFrame(input_data)
    
    # Create features ensuring consistent columns
    data = create_features(data, reference_data=reference_data)
    
    # Print data to ensure correct columns are included
    print(f"Data columns: {data.columns}")
    print(f"Reference data columns: {reference_data.columns}")
    print(f"Data shape: {data.shape}")
    print(f"Reference data shape: {reference_data.shape}")
    
    # Ensure 'net_worth' is present in the original dataset
    if 'net_worth' in original_data.columns:
        model, _, _ = train_model(reference_data)
        
        # Separate the new input data after one-hot encoding
        prediction = model.predict(data)
        
        return render_template('index.html', prediction=prediction[0], business_categories=business_categories)
    else:
        raise ValueError("Original dataset is missing 'net_worth' column.")

if __name__ == '__main__':
    app.run(debug=True)
