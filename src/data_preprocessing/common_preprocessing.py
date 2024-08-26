import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Load dataset from a CSV file.
    """
    return pd.read_csv(file_path)

def normalize_features(X):
    """
    Normalize numerical features using StandardScaler.
    """
    scaler = StandardScaler()
    return scaler.fit_transform(X)

def encode_categorical(df, columns):
    """
    Encode categorical variables using one-hot encoding.
    """
    return pd.get_dummies(df, columns=columns)

