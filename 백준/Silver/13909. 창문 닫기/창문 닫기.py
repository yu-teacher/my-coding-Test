end = int(input()) + 1
start = 1
trm = 1

while trm < end:
    start += 1
    trm = start ** 2

print(start - 1)