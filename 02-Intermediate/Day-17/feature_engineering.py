import pandas as pd
from sklearn.impute import SimpleImputer

def create_features(data, reference_data=None):
    # Ensure the 'age' column is present
    if 'age' not in data.columns:
        raise ValueError("Required column 'age' is missing.")
    
    # Convert 'gender' to numerical values
    gender_mapping = {'Male': 0, 'Female': 1}
    data['gender'] = data['gender'].map(gender_mapping)
    
    # One-Hot Encode 'business_category'
    data = pd.get_dummies(data, columns=['business_category'])
    
    if reference_data is not None:
        reference_columns = reference_data.columns.drop('net_worth')  # Drop 'net_worth'
        for column in reference_columns:
            if column not in data.columns:
                data[column] = 0  # Add missing columns with default value of 0
        data = data[reference_columns]
    
    # Handle any remaining NaNs
    imputer = SimpleImputer(strategy='mean')
    data = pd.DataFrame(imputer.fit_transform(data), columns=data.columns)
    
    return data
