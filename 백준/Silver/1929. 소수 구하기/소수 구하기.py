import sys
input = sys.stdin.readline
def del_list(num, plist):
    for i in range(len(plist)):
        if num * i >= len(plist):
            break
        plist[num * i] = 0


start, end = map(int, input().split())

primeList = [i for i in range(0, end+1)]

for i in primeList:
    if i == 1 or i == 0:
        continue
    if i != 0:
        del_list(i, primeList)
        if i >= start:
            print(i)