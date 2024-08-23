import unittest
import numpy as np
from src.models.xgboost_model import XGBoostModel
from src.models.lightgbm_model import LightGBMModel
from src.models.catboost_model import CatBoostModel
from src.models.dnn_model import DNNModel
from src.models.lstm_model import LSTMModel

class TestModels(unittest.TestCase):
    def setUp(self):
        self.X = np.random.rand(100, 10)
        self.y = np.random.randint(2, size=100)

    def test_xgboost_model(self):
        model = XGBoostModel({'n_estimators': 100})
        model.train(self.X, self.y)
        predictions = model.predict(self.X)
        self.assertEqual(len(predictions), 100)

    def test_lightgbm_model(self):
        model = LightGBMModel({'n_estimators': 100})
        model.train(self.X, self.y)
        predictions = model.predict(self.X)
        self.assertEqual(len(predictions), 100)

    def test_catboost_model(self):
        model = CatBoostModel({'iterations': 100})
        model.train(self.X, self.y)
        predictions = model.predict(self.X)
        self.assertEqual(len(predictions), 100)

    def test_dnn_model(self):
        model = DNNModel({'input_dim': 10})
        model.train(self.X, self.y)
        predictions = model.predict(self.X)
        self.assertEqual(len(predictions), 100)

    def test_lstm_model(self):
        X_lstm = self.X.reshape((100, 5, 2))
        model = LSTMModel({'timesteps': 5, 'features': 2})
        model.train(X_lstm, self.y)
        predictions = model.predict(X_lstm)
        self.assertEqual(len(predictions), 100)

if __name__ == '__main__':
    unittest.main() 
