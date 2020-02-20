from sklearn.model_selection import train_test_split
import pandas as pd

class AutoML:

    TEST_SIZE = 0.2
    NUMERICAL_VAL_STRATEGY = "median"

    def __init__(self, path: str, target: str, auto: bool=True):
        self.path = path
        self.target = target
        self._data = pd.read(self.path)
        if auto:
            self.preprocess()
        self.process()

    def preprocess(self):
        """
        1. Replace NA values
        2. Handle Categorical_features
        3. set design/target
        4. split test/train
        """
        self._handle_na_values()
        self._handle_cat_values()
        self._set_target_and_design()
        self._set_train_test()

    def process(self):
        pass

    def _set_target_and_design(self):
        """Set X (design) and y (target)"""
        self.y = self._data[self.target]
        self.X = self._data.loc[:, self._data.columns != self.target]

    def _set_train_test(self):
        """Split dataset into train/test parts."""
        (self.X_train, self.X_test, 
        self.y_train, self.y_test) = train_test_split(
                 X, self.y, test_size=self.__class__.TEST_SIZE)
    
    def _handle_cat_values(self):
        pass

    def _handle_na_values(self):
        pass


if __name__ == "__main__":
    model = AutoML(
        path='home/sevak/...', 
        target='price', 
        auto=False,
        )
