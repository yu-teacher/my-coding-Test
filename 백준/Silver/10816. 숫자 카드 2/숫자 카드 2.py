import sys
input = sys.stdin.readline

temp = input()
inList = list(map(int, input().split()))

temp = input()
reList = list(map(int, input().split()))

re_map = {}


for i in inList:
    if i in re_map:
        re_map[i] += 1
    else:
        re_map[i] = 1

for i in reList:
    if i in re_map:
        print(re_map[i], end=' ')
    else:
        print(0, end=' ')