import collections


def cache(n):
    d = collections.OrderedDict()

    def my_decorator(func):
        def my_my_decorator(*args, **kwargs):
            key = str(args) + str(kwargs)
            if key not in d:
                new_value = func(*args, **kwargs)
                if len(d) < n:
                    d[key] = new_value
                else:
                    d.popitem(last=False)
                    d[key] = new_value
                return new_value
            else:
                d.move_to_end(key, last=True)
                return d[key]
        my_my_decorator.__name__ = func.__name__
        my_my_decorator.__doc__ = func.__doc__
        my_my_decorator.__module__ = func.__module__
        my_my_decorator.next = 0
        return my_my_decorator
    return my_decorator
