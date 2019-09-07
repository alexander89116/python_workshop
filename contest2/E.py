n = int(input())
m = 2
while n != 0:
    d = 2
    t = 0
    while d * d <= m:
        if m % d == 0:
            t = 1
        d += 1
    if t == 0:
        n -= 1
        if n == 0:
            print(m)
    m += 1
