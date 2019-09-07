s = input()
mxl = 0
mxr = 0
n = len(s)


def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


for i in range(1, len(s) + 1):
    if is_palindrome(s[:i]):
        mxl = i

for i in range(len(s)):
    if is_palindrome(s[i:]):
        mxr = len(s) - i
        break

print(len(s) - max(mxl, mxr))
