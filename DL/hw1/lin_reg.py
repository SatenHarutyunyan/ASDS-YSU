import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class LinearRegressor:

    _LR_TYPES = ("analytic", "iterative", "sklearn")


    def __init__(self, lr_type: str):
        super().__init__()
        if lr_type not in self._LR_TYPES:
            raise ValueError(
                f"type_ must be one of {self._LR_TYPES}, instead got {type(lr_type)}")
        self.lr_type = lr_type
        self.W = None
        self.b = None
        self._loss = None


    @property
    def parameters(self) -> dict:
        return {
            "weights": self.W,
            "bias": self.b
        }


    @property
    def mse_loss(self) -> float:
        """Returns Measn Square Loss"""
        return float(self._loss)


    def learn_from(self, train_inp: tf.Tensor, train_out: tf.Tensor):
        """Learn from label data"""
        self._X_train = train_inp
        self._y_train = train_out
        ones: tf.Tensor = tf.ones(shape=train_inp._shape_tuple(), dtype=train_inp.dtype)
        X = tf.concat((ones, train_inp), axis=1)
        X_T: tf.Tensor = tf.transpose(X)
        y = train_out # for mathematical convinience
        if self.lr_type == "analytic":
            self._params: tf.Tensor = tf.matmul(tf.matmul(tf.linalg.inv(tf.matmul(X_T, X)), X_T), y)
        if self.lr_type == "iterative":
            iterations = 10000
            lr_rate=0.01
            theta = tf.ones((2,1))
            for it in range(iterations):
                prediction = tf.matmul(X, theta)
                theta = theta -(1 / len(y)) * lr_rate * tf.matmul(tf.transpose(X), (prediction - y))
            self._params = theta
        if self.lr_type == "sklearn":
            lin_reg = LinearRegression()
            lin_reg.fit(train_inp.numpy(),train_out.numpy())
            self._params = tf.constant([lin_reg.intercept_, lin_reg.coef_.flatten()])
        self.b = float(self._params[0])
        self.W = [float(i) for i in self._params[1]]


    def predict_for(self, test_inp: tf.Tensor):
        """Predict for unseen data"""
        self._test_inp = test_inp
        ones: tf.Tensor = tf.ones(shape=test_inp._shape_tuple(), dtype=test_inp.dtype)
        X = tf.concat((ones, test_inp), axis=1)
        self._y_pred = tf.matmul(X, self._params)
        self._loss = tf.reduce_mean(tf.square(test_inp - self._y_pred))
        return self._y_pred


    def show(self):
        plt.figure(figsize=(16, 10))
        plt.scatter(self._X_train, self._y_train, marker='o', color='blue')
        plt.plot(self._test_inp.numpy(), self._y_pred, color='red')
        plt.xlabel('X', fontsize=10)
        plt.ylabel('Y', fontsize=10)
        plt.legend(['regression line', 'data'])
        plt.show()
