import heapq


def merge_sorter(*args):
    hp = heapq.merge(*args)
    while True:
        try:
            yield next(hp)
        except StopIteration:
            break
