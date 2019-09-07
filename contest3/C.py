m = {}
s = input()
n = int(input())
i = 0
while n + i <= len(s):
    s1 = s[i:n + i]
    if s1 in m:
        m[s1] = m[s1] + 1
    else:
        m[s1] = 1
    i += 1
a = list()
for k in m.keys():
    if m[k] >= 2:
        a.append(k)
print(sorted(a))
