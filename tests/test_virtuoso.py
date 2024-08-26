import unittest
from src.virtuoso_framework import VIRTUOSOFramework
from src.utils import config

class TestVIRTUOSO(unittest.TestCase):

    def setUp(self):
        self.virtuoso_unsw = VIRTUOSOFramework('UNSW-NB15', use_weka=False)
        self.virtuoso_cse = VIRTUOSOFramework('CSE-CIC-IDS2018', use_weka=False)

    def test_unsw_preprocessing(self):
        X, y = self.virtuoso_unsw.preprocess(config['datasets']['UNSW-NB15']['path'])
        self.assertIsNotNone(X)
        self.assertIsNotNone(y)

    def test_cse_preprocessing(self):
        X, y = self.virtuoso_cse.preprocess(config['datasets']['CSE-CIC-IDS2018']['path'])
        self.assertIsNotNone(X)
        self.assertIsNotNone(y)

    def test_ml_engine(self):
        results = self.virtuoso_unsw.ml_engine.train_and_evaluate(
            [[1, 2, 3], [4, 5, 6]], [0, 1]
        )
        self.assertIsInstance(results, dict)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
