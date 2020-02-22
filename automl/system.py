from profile import Profile

class System:

    def __init__(self, profile: Profile):
        self.process()

    def process(self):
        self.pre_process()
        self.post_propecess()

    def pre_process(self):
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

    def post_process(self):
        raise NotImplementedError

    def _set_target_and_design(self):
        raise NotImplementedError

    def _set_train_test(self):
        raise NotImplementedError
    
    def _handle_cat_values(self):
        raise NotImplementedError

    def _handle_na_values(self):
        raise NotImplementedError


if __name__ == "__main__":
    profile = Profile()
    profile.ESTIMAOTR = "Ridge"
    profile.MODEL = "regression"
    profile.DATA = "/home/sevak/..."

    system = System(profile=profile)
    # system.predict()
