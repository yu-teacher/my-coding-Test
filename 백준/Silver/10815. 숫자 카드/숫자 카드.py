import sys

temp = int(input())
input_set = set(map(int, sys.stdin.readline().split()))
temp = int(input())
input_arr = list(map(int, sys.stdin.readline().split()))



for i in input_arr:
    if i in input_set:
        print('1',end=' ')
    else:
        print('0',end=' ')

