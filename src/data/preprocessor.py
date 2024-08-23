import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_unsw_nb15(data):
    X = data.drop(['attack_cat', 'label'], axis=1)
    y = data['attack_cat']
    
    X = pd.get_dummies(X)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

def preprocess_cse_cic_ids2018(data):
    X = data.drop('Label', axis=1)
    y = data['Label']
    
    X = pd.get_dummies(X)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

def preprocess_data(unsw_data, cse_data):
    unsw_result = preprocess_unsw_nb15(unsw_data)
    cse_result = preprocess_cse_cic_ids2018(cse_data)
    return unsw_result, cse_result
