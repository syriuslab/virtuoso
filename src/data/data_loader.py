import pandas as pd

def load_unsw_nb15(path):
    """Load UNSW-NB15 dataset"""
    return pd.read_csv(path)

def load_cse_cic_ids2018(path):
    """Load CSE-CIC-IDS2018 dataset"""
    return pd.read_csv(path)

def load_data(unsw_path, cse_path):
    unsw_data = load_unsw_nb15(unsw_path)
    cse_data = load_cse_cic_ids2018(cse_path)
    return unsw_data, cse_data
