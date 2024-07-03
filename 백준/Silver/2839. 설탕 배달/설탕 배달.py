data = int(input())

count_5 = 0
count_3 = 0
sumNum = 0

while data > sumNum:
    count_5 += 1
    sumNum += 5

while count_5 > 0:
    if data < sumNum:
        count_5 -= 1
        count_3 += 1
        sumNum -= 2
    elif data > sumNum:
        count_3 += 1
        sumNum += 3
    else:
        break

if data == sumNum:
    print(count_5 + count_3)
else:
    print(-1)