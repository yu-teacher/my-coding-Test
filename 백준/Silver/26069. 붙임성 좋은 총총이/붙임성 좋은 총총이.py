import sys

input = sys.stdin.readline

check_set = {'ChongChong'}

start_gom = False

for _ in range(int(input())):
    n, m = input().split()
    if n == 'ChongChong' or m == 'ChongChong':
        start_gom = True
    if start_gom:
        if m in check_set:
            check_set.add(n)
        elif n in check_set:
            check_set.add(m)

print(len(check_set))