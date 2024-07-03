import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
i, j = map(int, input().split())

top = n*j + m*i
bom = m*j
gcd = math.gcd(top, bom)
print(top//gcd, end=' ')
print(bom//gcd)


 