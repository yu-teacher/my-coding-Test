import sys
numList = [0] * 10001  

for i in range(int(input())):
    numList[int(sys.stdin.readline())] += 1

for index, value in enumerate(numList):
    if value != 0:
        for _ in range(value):
            print(index)
