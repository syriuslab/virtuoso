import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_features(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)

def encode_categorical(df, columns):
    return pd.get_dummies(df, columns=columns)
