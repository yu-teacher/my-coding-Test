count = 1
checkNum = 1
data = int(input())

while data > checkNum:
    checkNum += count * 6
    count += 1

print(count)