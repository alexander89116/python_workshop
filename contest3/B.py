keys = list(input())
values = list(input())
d = len(keys) - len(values)
for i in range(0, d):
    values.append(None)
a = dict(zip(keys, values))
print(sorted(a.items()))
