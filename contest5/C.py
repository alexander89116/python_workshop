f = open("input.txt")


def parse(s):
    a = s.split("\t")
    print(a[0][:7], "."*(73 - len(a[4])), a[4], sep="")


for line in f:
    if line != "\n":
        parse(line.strip("\n"))
