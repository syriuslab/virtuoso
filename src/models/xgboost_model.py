from xgboost import XGBClassifier

class XGBoostModel:
    def __init__(self, params):
        self.model = XGBClassifier(**params)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)
