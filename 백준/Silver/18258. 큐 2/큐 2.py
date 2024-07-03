from collections import deque
import sys

input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    comment = input().split()

    if comment[0] == 'push':
        q.append(int(comment[1]))
    elif comment[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif comment[0] == 'size':
        print(len(q))
    elif comment[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif comment[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif comment[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
