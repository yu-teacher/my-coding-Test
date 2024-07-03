numList = [int(input()) for i in range(5)]
numList.sort()
print(sum(numList) // len(numList))
print(numList[2])