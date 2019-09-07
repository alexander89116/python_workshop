n = int(input())
ans = ""
for i in range(1, n):
    if i % 15 == 0:
        ans += "Fizz Buzz, "
    elif i % 5 == 0:
        ans += "Buzz, "
    elif i % 3 == 0:
        ans += "Fizz, "
    else:
        ans += (str(i) + ", ")
if n % 15 == 0:
    ans += "Fizz Buzz"
elif n % 5 == 0:
    ans += "Buzz"
elif n % 3 == 0:
    ans += "Fizz"
else:
    ans += str(n)
print(ans)
