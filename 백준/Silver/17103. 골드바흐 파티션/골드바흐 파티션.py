def zero_list(num, lst):
    for i in range(num, len(lst), num):
        lst[i] = 0


numList = [i for i in range(1000000)]
primeList = []

for i in numList:
    if i < 2:
        continue
    if i != 0:
        primeList.append(i)
        zero_list(i, numList)

primeSet = set(primeList)

for i in range(int(input())):
    temp = int(input())
    print(sum([1 for j in primeList if temp - j in primeSet and temp//2 <= temp - j]))