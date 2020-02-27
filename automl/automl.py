import os

import numpy

from descriptors import (
    device, estimator, model, data, target
)

class Profile:

    device = device.Device()
    estimator = estimator.Estimator()
    model = model.Model()
    data = data.Data()
    target = target.Target()


class System:

    def __init__(self, profile: Profile):
        self._profile = profile

    def run(self):
        self.__pre_process()
        self.__post_propecess()

    def __pre_process(self):
        """Prepare the dataset for estimator."""
        self.__handle_na_values()
        self.__handle_cat_values()
        self.__set_target_and_design()
        self.__set_train_test()

    def __post_process(self):
        """"""
        raise NotImplementedError

    def __set_target_and_design(self) -> None:
        """Simple function that splits the dataset,
        into X (design) and y (target)."""
        raise NotImplementedError

    def __set_train_test(self) -> None:
        """Simple function that splits the dataset,
        into X_train, X_test, y_train, y_test."""
        
    
    def __handle_cat_values(self) -> None:
        """Simple function that detects categorical features,
        and transforms their type into numerical."""
        raise NotImplementedError

    def __handle_na_values(self) -> None:
        """Simple function that detects missing values,
        and transforms their type into numerical."""
        raise NotImplementedError


if __name__ == "__main__":

    profile = Profile()

    profile.data =  input("Enter the location of data: ")
    profile.target = input("Enter the name or index of the target: ")
    profile.model = input("Enter the model type [regression|classification]: ")
    profile.estimator = input("Enter the type of the estimator: ")
    profile.device = input("Enter the type of the device (default is CPU ): ")

    system = System(profile=profile)
    print(system._profile.data)
    # system.run()
