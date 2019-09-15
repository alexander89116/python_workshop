import sys
import traceback


def force_load(file):
    ldict = {}
    lines = []
    with open(file + '.py', 'r') as f:
        for i in f:
            lines.append(i)

    while True:
        try:
            exec(''.join(lines), globals(), ldict)
            break
        except SyntaxError as error:
            del lines[error.lineno - 1]
        except Exception as error:
            a = sys.exc_info()
            del lines[traceback.extract_tb(a[2])[-1][1] - 1]

    return ldict
