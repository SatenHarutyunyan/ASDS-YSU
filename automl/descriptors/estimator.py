class Estimator:

    _estimators = ("Ridge", "Lasso")

    def __init__(self):
        self._data = {}
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass
