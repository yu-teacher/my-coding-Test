from itertools import permutations

n, m = map(int, input().split())
nums = [i + 1 for i in range(n)]
perm = list(permutations(nums, m))

for i in perm:
    for j in i:
        print(j, end=' ')
    print()