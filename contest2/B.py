n = int(input())
cnt1 = 1000000
cnt2 = 1000000
for i in range(n, 1000000):
    j = i
    c1 = j % 10
    j //= 10
    c1 += j % 10
    j //= 10
    c1 += j % 10
    j //= 10
    c2 = j % 10
    j //= 10
    c2 += j % 10
    j //= 10
    c2 += j % 10
    if c1 == c2:
        cnt2 = i - n
        break

for i in range(1, n - 100000):
    j = n - i
    c1 = j % 10
    j //= 10
    c1 += j % 10
    j //= 10
    c1 += j % 10
    j //= 10
    c2 = j % 10
    j //= 10
    c2 += j % 10
    j //= 10
    c2 += j % 10
    if c1 == c2:
        cnt1 = i
        break
if cnt1 <= cnt2:
    ans = n - cnt1
    print(ans)
else:
    ans = n + cnt2
    print(ans)
