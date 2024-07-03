import sys
input = sys.stdin.readline

n, m = map(int, input().split())

key_dict = {}
val_dict = {}

for i in range(1, n + 1):
    val = input().strip()
    key_dict[i] = val
    val_dict[val] = i

for i in range(m):
    val = input().strip()
    if val.isdigit():
        print(key_dict[int(val)])
    else:
        print(val_dict[val])