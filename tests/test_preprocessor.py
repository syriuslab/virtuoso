import unittest
import pandas as pd
import numpy as np
from src.data.preprocessor import preprocess_unsw_nb15, preprocess_cse_cic_ids2018

class TestPreprocessor(unittest.TestCase):
    def test_preprocess_unsw_nb15(self):
        data = pd.DataFrame({
            'feature1': np.random.rand(100),
            'feature2': np.random.choice(['A', 'B', 'C'], 100),
            'attack_cat': np.random.choice(['normal', 'attack'], 100),
            'label': np.random.choice([0, 1], 100)
        })
        X_train, X_test, y_train, y_test = preprocess_unsw_nb15(data)
        self.assertEqual(X_train.shape[1], X_test.shape[1])
        self.assertEqual(len(y_train) + len(y_test), len(data))

    def test_preprocess_cse_cic_ids2018(self):
        data = pd.DataFrame({
            'feature1': np.random.rand(100),
            'feature2': np.random.choice(['A', 'B', 'C'], 100),
            'Label': np.random.choice(['BENIGN', 'ATTACK'], 100)
        })
        X_train, X_test, y_train, y_test = preprocess_cse_cic_ids2018(data)
        self.assertEqual(X_train.shape[1], X_test.shape[1])
        self.assertEqual(len(y_train) + len(y_test), len(data))

if __name__ == '__main__':
    unittest.main()
