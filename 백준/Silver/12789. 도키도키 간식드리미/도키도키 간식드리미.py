import sys
input = sys.stdin.readline

num = int(input())
in_list = list(map(int, input().split()))
stack = []
flag = True

count = 1

while flag:
    len_in_list = len(in_list)
    len_stack = len(stack)

    if in_list and in_list[0] == count:
        del in_list[0]
        count += 1
    elif stack and stack[-1] == count:
        stack.pop()
        count += 1
    elif in_list:
        stack.append(in_list[0])
        del in_list[0]

    if len_in_list == len(in_list) and len_stack == len(stack):
        flag = False

if in_list or stack:
    print('Sad')
else:
    print('Nice')