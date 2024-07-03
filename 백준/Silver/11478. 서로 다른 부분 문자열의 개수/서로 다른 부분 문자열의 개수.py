inStr = input()
reSet = set()

for i in range(len(inStr)):
    tempNum = len(inStr) - i
    for j in range(tempNum):
        reSet.add(inStr[j:j + i + 1])

print(len(reSet))