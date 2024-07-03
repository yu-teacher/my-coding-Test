data = int(input())
numList = [int(input()) for i in range(data)]
numList.sort()
for num in numList: 
    print(num)
