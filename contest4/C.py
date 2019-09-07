import sys


def takes(*args1):
    def my_decorator(func):
        def my_my_dec(*args2):
            for i in range(min(len(args1), len(args2))):
                if not isinstance(args2[i], args1[i]):
                    raise TypeError
            return func(*args2)
        my_my_dec.__name__ = func.__name__
        my_my_dec.__doc__ = func.__doc__
        my_my_dec.__module__ = func.__module__
        return my_my_dec
    return my_decorator


exec(sys.stdin.read())
