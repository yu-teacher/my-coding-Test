import sys

data = int(input())
numList = [int(sys.stdin.readline().rstrip()) for i in range(data)]
numList.sort()
for num in numList:
    print(num)