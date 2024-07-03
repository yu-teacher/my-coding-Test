from itertools import combinations

n, max_value = map(int, input().split())
numList = list(map(int, input().split()))

maxSum = 0  

for combo in combinations(numList, 3):
    current_sum = sum(combo)
    if current_sum <= max_value:
        maxSum = max(maxSum, current_sum)

print(maxSum)
