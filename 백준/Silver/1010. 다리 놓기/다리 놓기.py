import math
for _ in range(int(input())):
    n,m = map(int, input().split())
    print(math.comb(m,n))