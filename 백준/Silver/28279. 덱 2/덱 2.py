from collections import deque
import sys
input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    content = list(map(int, input().split()))

    if content[0] == 1:
        q.appendleft(content[1])
    elif content[0] == 2:
        q.append(content[1])
    elif content[0] == 3:
        if q:
            print(q[0])
            del q[0]
        else:
            print(-1)
    elif content[0] == 4:
        if q:
            print(q[-1])
            q.pop()
        else:
            print(-1)
    elif content[0] == 5:
        print(len(q))
    elif content[0] == 6:
        if q:
            print(0)
        else:
            print(1)
    elif content[0] == 7:
        if q:
            print(q[0])
        else:
            print(-1)
    elif content[0] == 8:
        if q:
            print(q[-1])
        else:
            print(-1)