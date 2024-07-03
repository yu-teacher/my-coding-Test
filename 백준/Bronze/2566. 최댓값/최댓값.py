arr = [list(map(int, input().split())) for _ in range(9)]
maxNum = 0
max_row = 1
max_col = 1 

for iIndex, row in enumerate(arr):
    for jIndex, cal in enumerate(row):
        if maxNum < cal:
            maxNum = cal
            max_row = iIndex+1
            max_col = jIndex+1  

print(maxNum)
print(max_row,' ',max_col) 
    