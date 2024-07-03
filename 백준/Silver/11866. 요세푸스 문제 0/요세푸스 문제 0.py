import sys

input = sys.stdin.readline

m, n = map(int, input().split())
t = n - 1
osps = [i+1 for i in range(m)]
re_list = []

while osps:
    for _ in range(n-1):
        osps.append(osps[0])
        del osps[0]
    re_list.append(osps[0])
    del osps[0]

print("<" + ", ".join(map(str, re_list)) + ">")