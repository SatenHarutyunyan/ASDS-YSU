
# TODO: 
#1  if model is set, then make sure that only that model estimators can be set
#2 if estimator is set, then make sure that the user cannot pass invalid model type
#3 change name of profile to smth else

__all__ : tuple = ("Profile",)

class Estimator:

    # estimators = None
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class Model:

    models = ("regression", "classification")

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class Device:

    devices = ("GPU", "CPU")
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class Data:

    # data = (".csv", ".tsv", "")
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class Profile:

    DEVICE = Device()
    ESTIMATOR = Estimator()
    MODEL = Model()
    DATA = Data()


if __name__ == "__main__":
    profile = Profile() # "gpu", "cpu" (Lowercase & Uppercase)
    profile.DEVICE = "GPU" # "regression", "classification" (Spell check, lower & upper)
    profile.MODEL = "regression" 
    profile.ESTIMAOTR = "Ridge" # support db, cloud, web, local (determine the type ie. extensions)
    profile.DATA = "/home/sevak/..." 

    print(
        profile.DEVICE
    )