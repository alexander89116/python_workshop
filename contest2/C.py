n, m = map(int, input().split())
for i in range(1, n + 1):
    s = ""
    for j in range(1, m + 1):
        s += str(i * j)
        s += " "
    print(s)
