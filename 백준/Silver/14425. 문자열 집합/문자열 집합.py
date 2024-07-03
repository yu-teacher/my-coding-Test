import sys
input = sys.stdin.readline

n,m = map(int, input().split())
count = 0
nSet = {input() for i in range(n)}
mList = [input() for i in range(m)]

for i in mList:
    if i in nSet:
        count += 1

print(count)