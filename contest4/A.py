def pascal_triangle():
    a = [1]
    while 1 == 1:
        i = 0
        while i < len(a):
            yield a[i]
            i += 1
        b = list()
        b.append(1)
        for j in range(len(a) - 1):
            b.append(a[j] + a[j + 1]);
        b.append(1)
        a = b[:]
