import sys
input = sys.stdin.readline

re_dict = {}
re_List = []

for i in range(int(input())):
    name, status = input().split()
    re_dict[name] = status

for key, val in re_dict.items():
    if val == 'enter':
        re_List.append(key)
        
re_List.sort(reverse = True)

for i in re_List:
    print(i)