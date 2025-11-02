from .common_preprocessing import load_data, normalize_features, encode_categorical

def preprocess_CSE_CIC_IDS2018(file_path):
    """
    Preprocess the CSE-CIC-IDS2018 dataset.
    """
    df = load_data(file_path)
    
    # Identify categorical columns (adjust as needed)
    categorical_columns = ['Protocol', 'Timestamp']
    
    # Encode categorical variables
    df = encode_categorical(df, categorical_columns)
    
    # Separate features and target
    X = df.drop('Label', axis=1)
    y = df['Label']
    
    # Normalize features
    X_normalized = normalize_features(X)
    
    return X_normalized, y
