
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

    # data =  support db, cloud, web, local (determine the type ie. extensions)
    
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass

class Target:

    # target = either index of string 
        
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class Profile:

    device = Device()
    estimator = Estimator()
    model = Model()
    data = Data()
    target = Target()
