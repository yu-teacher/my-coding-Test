import sys
input = sys.stdin.readline

n, m = map(int, input().split())  
liList = [input().strip() for i in range(n)]  
loSet = set(input().strip() for i in range(m))  

re_list = []

for i in liList:
    if i in loSet:
        re_list.append(i)

print(len(re_list))
re_list.sort()
for i in re_list:
    print(i)
        
