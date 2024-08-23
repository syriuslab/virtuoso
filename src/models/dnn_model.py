from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class DNNModel:
    def __init__(self, params):
        self.model = Sequential([
            Dense(64, activation='relu', input_shape=(params['input_dim'],)),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, X, y):
        self.model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

    def predict(self, X):
        return (self.model.predict(X) > 0.5).astype("int32")
