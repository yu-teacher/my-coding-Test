data = int(input())

count = 0
checkNum = 666

while True:  
    Count_6 = 0
    tempStr = str(checkNum)
    for i in tempStr:
        if i == '6':
            Count_6 += 1
            if Count_6 >= 3:
                break  
        else:
            Count_6 = 0
    
    if Count_6 >= 3:
        count += 1
        if count == data:
            print(checkNum)
            break  
    checkNum += 1
