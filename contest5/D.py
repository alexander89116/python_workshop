password = input()


def check(s):
    if len(password) < 8:
        print("weak")
        return
    if len(set(s)) < 4:
        print("weak")
        return
    if "anna" in s.lower():
        print("weak")
        return
    if s == s.lower():
        print("weak")
        return
    if s == s.upper():
        print("weak")
        return
    alpha = 0
    digit = 0
    for c in s:
        if c.isalpha():
            alpha = 1
    for c in s:
        if c.isdigit():
            digit = 1
    if alpha == 0 or digit == 0:
        print("weak")
        return
    print("strong")


check(password)
