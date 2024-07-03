import sys

input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    in_num = int(input())
    if in_num != 0:
        stack.append(in_num)
    else:
        stack.pop()

print(sum(stack))