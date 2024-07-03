data = int(input())

selNum = 0
is_end = True

for i in range(data):
    tempNum = i + sum(int(t) for t in str(i))
    if tempNum == data:
        is_end = False
        selNum = i
        break
        
if is_end:
    print(0)
else:
    print(selNum)