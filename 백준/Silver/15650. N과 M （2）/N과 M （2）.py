from itertools import combinations

n, m = map(int, input().split())
nums = [i + 1 for i in range(n)]
combi = list(combinations(nums, m))

for i in combi:
    for j in i:
        print(j, end=' ')
    print()