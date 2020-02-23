from profile import Profile


class System:

    def __init__(self, profile: Profile):
        self.__profile = profile

    def run(self):
        self.__pre_process()
        self.__post_propecess()

    def __pre_process(self):
        """Prepare the dataset for estimator."""
        self._handle_na_values()
        self._handle_cat_values()
        self._set_target_and_design()
        self._set_train_test()

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
        raise NotImplementedError
    
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
    profile.data = "/home/sevak/..."
    profile.model = "regression" 
    profile.estimator = "Ridge"
    profile.target = "price"
    profile.device = "GPU"

    system = System(profile=profile)
    system.run()
