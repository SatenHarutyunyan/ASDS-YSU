import enum

__all__ = ("Data", )



class Target:
    pass


class _Extension(enum.Enum):
    csv = '.csv'
    tsv = '.tsv'
    xlsx = '.xlsx'


class Data:

    target = Target()
    extension = _Extension()

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass
