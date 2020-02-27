import enum


__all__ = ("Model", )


class Estimator(enum.Enum):
    Lasso = "Lasso"
    Ridge = "Ridge"


class Model:

    estimator = Estimator()

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):                                        
        pass
