from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = [i + 1 for i in range(n)]

for i in combinations_with_replacement(nums, m):
    for j in i:
        print(j, end=' ')
    print()