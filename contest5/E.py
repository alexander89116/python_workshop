import import_me


def get_all_functions():
    ans = []
    for i in dir(import_me)[8:]:
        if callable(getattr(import_me, i)):
            ans.append(i)
    return ans
