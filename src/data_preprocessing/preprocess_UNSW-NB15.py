from .common_preprocessing import load_data, normalize_features, encode_categorical

def preprocess_UNSW_NB15(file_path):
    """
    Preprocess the UNSW-NB15 dataset.
    
    This function performs the following steps:
    1. Load the data from the specified file path
    2. Drop unnecessary columns
    3. Encode categorical variables
    4. Separate features and target
    5. Normalize features
    
    Args:
    file_path (str): Path to the UNSW-NB15 dataset file.
    
    Returns:
    tuple: A tuple containing:
        - X_normalized (numpy.ndarray): Normalized feature matrix
        - y (pandas.Series): Target variable
    """
    # Load the dataset
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

# Example usage (can be removed if not needed)
if __name__ == "__main__":
    file_path = "path/to/UNSW-NB15_dataset.csv"
    X, y = preprocess_UNSW_NB15(file_path)
    print("Preprocessing completed. X shape:", X.shape, "y shape:", y.shape)
