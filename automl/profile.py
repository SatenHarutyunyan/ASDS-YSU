
# TODO: 
#1  if model is set, then make sure that only that model estimators can be set
#2 if estimator is set, then make sure that the user cannot pass invalid model type
#3 change name of profile to smth else

__all__ = ("Profile",)

class __Estimator:
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class __Model:

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class __Device:
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class __Data:
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class Profile:

    DEVICE = __Device()
    ESTIMATOR = __Estimator()
    MODEL = __Model()
    DATA = __Data()


if __name__ == "__main__":
    profile = Profile() # "gpu", "cpu" (Lowercase & Uppercase)
    profile.DEVICE = "GPU" # "regression", "classification" (Spell check, lower & upper)
    profile.MODEL = "regression" 
    profile.ESTIMAOTR = "Ridge" # support db, cloud, web, local (determine the type ie. extensions)
    profile.DATA = "/home/sevak/..." 
