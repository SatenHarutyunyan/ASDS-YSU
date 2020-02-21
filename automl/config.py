from descriptors import (
    Estimator, Model
)


class Config:
    ESTIMAOTR = Estimator()
    MODEL = Model()



if __name__ == "__main__":
    cfg = Config()
    cfg.MODEL = "regression"
    cfg.ESTIMAOTR = "Ridge"
