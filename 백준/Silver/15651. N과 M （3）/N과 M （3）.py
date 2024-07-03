from itertools import product

n, m = map(int, input().split())
nums = [i + 1 for i in range(n)]

for i in product(nums, repeat=m):
    for j in i:
        print(j, end=' ')
    print()