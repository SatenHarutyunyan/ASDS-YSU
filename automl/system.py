from profile import Profile

class System:

    def __init__(self, profile: Profile):
        self.__profile = profile

    # @property
    # def profile(self):
    #     """Alias for self.__profile"""
    #     return self.__profile

    # @profile.setter
    # def profile(self, _):
    #     self.__profile = self.__profile

    def run(self):
        self.__pre_process()
        self.__post_propecess()

    def __pre_process(self):
        """
        1. handle NA values
        2. handle categorical features
        3. set design/target
        4. split test/train
        """
        self._handle_na_values()
        self._handle_cat_values()
        self._set_target_and_design()
        self._set_train_test()

    def __post_process(self):
        raise NotImplementedError

    def __set_target_and_design(self) -> None:
        raise NotImplementedError

    def __set_train_test(self) -> None:
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
    profile.ESTIMAOTR = "Ridge"
    profile.MODEL = "regression"
    profile.DATA = "/home/sevak/..."

    system = System(profile=profile)

    system.run()
