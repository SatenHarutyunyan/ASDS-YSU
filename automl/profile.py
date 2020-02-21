
#TODO:
# if model is set, then make sure that only that model estimators can be set
# if estimator is set, then make sure that the user cannot pass invalid model type

class _Estimator:
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class _Model:

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class _Device:
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class _Data:
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class Profile:

    DEVICE = _Device()
    ESTIMATOR = _Estimator()
    MODEL = _Model()
    DATA = _Data()


if __name__ == "__main__":
    profile = Profile()
    # "gpu", "cpu" (Lowercase & Uppercase)
    profile.DEVICE = "GPU"
    # "regression", "classification" (Spell check, lower & upper)
    profile.MODEL = "regression" 
    #  
    profile.ESTIMAOTR = "Ridge"
    # support db, cloud, web, local (determine the type ie. extensions)
    profile.DATA = "/home/sevak/..." 
    #