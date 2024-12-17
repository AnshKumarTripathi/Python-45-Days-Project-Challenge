import pandas as pd
from sklearn.impute import SimpleImputer

def load_data(filepath):
    data = pd.read_csv(filepath, low_memory=False)
    
    def convert_net_worth(value):
        if 'B' in value:
            return float(value.replace(' B', '')) * 1e9
        elif 'M' in value:
            return float(value.replace(' M', '')) * 1e6
        else:
            return float(value)
    
    # Apply conversion to 'net_worth' column
    data['net_worth'] = data['net_worth'].apply(convert_net_worth)
    
    # Separate numerical and categorical columns
    numerical_cols = ['age', 'net_worth']
    categorical_cols = ['gender', 'business_category']
    
    # Handle missing values using imputation for numerical columns
    num_imputer = SimpleImputer(strategy='mean')
    data[numerical_cols] = num_imputer.fit_transform(data[numerical_cols])
    
    # Handle missing values in categorical columns (e.g., using 'most_frequent' strategy)
    cat_imputer = SimpleImputer(strategy='most_frequent')
    data[categorical_cols] = cat_imputer.fit_transform(data[categorical_cols])
    
    # Drop unnecessary columns
    columns_to_keep = numerical_cols + categorical_cols
    data = data[columns_to_keep]
    data = data.dropna()
    return data
