import collections.abc
from app import VeryImportantClass, decorator


class HackedClass(VeryImportantClass):

    def __init__(self, *args):
        super().__init__(*args)

    def __getattribute__(self, item):
        if item[0] == '_':
            return VeryImportantClass.__getattribute__(self, item)
        if callable(VeryImportantClass.__getattribute__(self, item)):
            return decorator(VeryImportantClass.__getattribute__(self, item))
        if isinstance(VeryImportantClass.__getattribute__(self, item), int) or isinstance(
                VeryImportantClass.__getattribute__(self, item), float):
            return VeryImportantClass.__getattribute__(self, item) * 2
        if isinstance(VeryImportantClass.__getattribute__(self, item), collections.abc.Iterable):
            return type(VeryImportantClass.__getattribute__(self, item))()
        return VeryImportantClass.__getattribute__(self, item)
