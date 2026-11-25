
class LinearRegression:
    def __init__(self, learning_rate=0.01, epochs=2000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weight = 0.0
        self.bias = 0.0

    def fit(self, X, y):
        n = len(X)

        for _ in range(self.epochs):
            predictions = self.predict(X)

            dw = (-2 / n) * sum(
                x * (actual - predicted)
                for x, actual, predicted
                in zip(X, y, predictions)
            )

            db = (-2 / n) * sum(
                actual - predicted
                for actual, predicted
                in zip(y, predictions)
            )

            self.weight -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        return [
            self.weight * x + self.bias
            for x in X
        ]


if __name__ == "__main__":
    X = [1, 2, 3, 4, 5]
    y = [3, 5, 7, 9, 11]

    model = LinearRegression()
    model.fit(X, y)

    print(f"Weight: {model.weight:.4f}")
    print(f"Bias: {model.bias:.4f}")
    print(f"Prediction: {model.predict([6])[0]:.4f}")
