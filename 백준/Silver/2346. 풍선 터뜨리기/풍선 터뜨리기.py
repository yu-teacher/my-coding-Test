import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
content = list(map(int, input().split()))
dq = deque([[i + 1, content[i]] for i in range(num)])
re_list = []

for _ in range(num):
    temp_index = dq[0][1]
    re_list.append(dq[0][0])
    dq.popleft()
    term = 1 if temp_index > 0 else -1
    if term > 0:
        temp_index -= term
    while temp_index != 0:
        temp_index -= term
        if not dq:
            break
        if term > 0:
            dq.append(dq.popleft())
        else:
            dq.appendleft(dq.pop())

print(' '.join(map(str, re_list)))