import unittest
import pandas as pd
from src.data.data_loader import load_unsw_nb15, load_cse_cic_ids2018

class TestDataLoader(unittest.TestCase):
    def test_load_unsw_nb15(self):
        data = load_unsw_nb15('path/to/test/UNSW-NB15_1.csv')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)
        self.assertIn('attack_cat', data.columns)

    def test_load_cse_cic_ids2018(self):
        data = load_cse_cic_ids2018('path/to/test/CSE-CIC-IDS2018.csv')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)
        self.assertIn('Label', data.columns)

if __name__ == '__main__':
    unittest.main()
