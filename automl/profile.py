from automl.descriptors import model, data


class Profile:

    __slots__ = ("model", "data")

    model = model.Model()
    data = data.Data()