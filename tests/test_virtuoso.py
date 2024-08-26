import unittest
import pandas as pd
import numpy as np
from src.data_preprocessing.preprocess_UNSW_NB15 import preprocess_UNSW_NB15
from src.data_preprocessing.preprocess_CSE_CIC_IDS2018 import preprocess_CSE_CIC_IDS2018

class TestVIRTUOSO(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame that mimics the structure of UNSW-NB15
        self.sample_unsw = pd.DataFrame({
            'id': [1, 2, 3],
            'proto': ['tcp', 'udp', 'tcp'],
            'service': ['http', 'dns', 'smtp'],
            'state': ['CON', 'INT', 'CON'],
            'label': [0, 1, 0],
            'attack_cat': ['Normal', 'DoS', 'Normal']
        })

        # Create a sample DataFrame that mimics the structure of CSE-CIC-IDS2018
        self.sample_cse = pd.DataFrame({
            'Timestamp': ['2018-02-14 09:15:00', '2018-02-14 09:16:00'],
            'Protocol': ['TCP', 'UDP'],
            'Label': ['BENIGN', 'DoS']
        })

    def test_preprocess_UNSW_NB15(self):
        # Mock the load_data function to return our sample data
        import src.data_preprocessing.common_preprocessing
        src.data_preprocessing.common_preprocessing.load_data = lambda x: self.sample_unsw

        X, y = preprocess_UNSW_NB15("dummy_path")
        
        self.assertIsInstance(X, np.ndarray)
        self.assertIsInstance(y, pd.Series)
        self.assertEqual(X.shape[0], 3)  # 3 samples
        self.assertEqual(y.shape[0], 3)  # 3 labels

    def test_preprocess_CSE_CIC_IDS2018(self):
        # Mock the load_data function to return our sample data
        import src.data_preprocessing.common_preprocessing
        src.data_preprocessing.common_preprocessing.load_data = lambda x: self.sample_cse

        X, y = preprocess_CSE_CIC_IDS2018("dummy_path")
        
        self.assertIsInstance(X, np.ndarray)
        self.assertIsInstance(y, pd.Series)
        self.assertEqual(X.shape[0], 2)  # 2 samples
        self.assertEqual(y.shape[0], 2)  # 2 labels

if __name__ == '__main__':
    unittest.main()
