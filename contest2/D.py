a0 = 0
a1 = 1
n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        t = a0 + a1
        a0 = a1
        a1 = t
    print(a1)
