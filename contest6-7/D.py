import sys
import traceback

from contextlib import contextmanager


@contextmanager
def retyper(*args):
    try:
        yield
    except args[0] as error:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        ans = args[1](exc_value.args[0]).with_traceback(exc_traceback)
        ans.args = exc_value.args
        raise ans


@contextmanager
def supresser(*args):
    try:
        yield
    except Exception as e:
        a = sys.exc_info()
        if a[0] in args:
            pass
        else:
            raise


@contextmanager
def dumper(stream):
    try:
        yield
    except Exception as e:
        a = sys.exc_info()
        formatted_lines = traceback.format_exc().splitlines()
        print(formatted_lines[-1], file=stream)
        raise

