from .common_preprocessing import load_data, normalize_features, encode_categorical

def preprocess_UNSW_NB15(file_path):
    """
    Preprocess the UNSW-NB15 dataset.
    """
    df = load_data(file_path)
    
    # Drop unnecessary columns
    df = df.drop(['id', 'attack_cat'], axis=1)
    
    # Encode categorical variables
    categorical_columns = ['proto', 'service', 'state']
    df = encode_categorical(df, categorical_columns)
    
    # Separate features and target
    X = df.drop('label', axis=1)
    y = df['label']
    
    # Normalize features
    X_normalized = normalize_features(X)
    
    return X_normalized, y
