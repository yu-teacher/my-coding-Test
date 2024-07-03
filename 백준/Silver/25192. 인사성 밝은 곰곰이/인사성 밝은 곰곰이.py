import sys
input = sys.stdin.readline

in_list = []
user = set()
re_num = 0

for _ in range(int(input())):
    in_list.append(input().strip())

for i in in_list:
    if i == 'ENTER':
        re_num += len(user)
        user.clear()
    else:
        user.add(i)
re_num += len(user)
print(re_num)