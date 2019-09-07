import time

tm = time.time()


def profiler(func):

    def my_decorator(*args):
        if my_decorator.cnt == 0:
            my_decorator.calls = 0
            global tm
            tm = time.time()
        my_decorator.calls += 1
        my_decorator.last_time_taken = time.time() - tm
        my_decorator.cnt += 1
        x = func(*args)
        my_decorator.cnt -= 1
        return x

    my_decorator.__name__ = func.__name__
    my_decorator.__doc__ = func.__doc__
    my_decorator.__module__ = func.__module__
    my_decorator.calls = 00
    my_decorator.last_time_taken = 00
    my_decorator.cnt = 0
    return my_decorator
