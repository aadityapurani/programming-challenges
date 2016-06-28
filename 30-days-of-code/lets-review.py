#Day 6 Lets Review HackerRank
#Coded By Aaditya Purani
n = int(raw_input().strip())


def walk(line):
    first = []
    second = []
    for i, c in enumerate(line):
        if i % 2 == 0:
            first.append(c)
        else:
            second.append(c)
    out = "".join(first) + " " + "".join(second)
    return out


for i in range(n):
    line = raw_input()
    print(walk(line))
