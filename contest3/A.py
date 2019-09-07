s = input().split()
a = {}
m = 0
for i in s:
    if i in a:
        a[i] = a[i] + 1
        if m < a[i]:
            m = a[i]
    else:
        a[i] = 1
print(m / len(s))
