import sys
import math

input = sys.stdin.readline


def find_gcd_of_list(numbers):
    result_gcd = numbers[0]
    for num in numbers[1:]:
        result_gcd = math.gcd(result_gcd, num)
    return result_gcd


namuLen = int(input())
namuList = [int(input()) for i in range(namuLen)]
trumList = list()

for i in range(len(namuList) - 1):
    trumList.append(namuList[i + 1] - namuList[i])

trum = find_gcd_of_list(trumList)

print(abs((namuList[-1] - namuList[0]) // trum + 1 - namuLen))