import sys

input = sys.stdin.readline


def recursion(s, l, r):
    global function_calls
    function_calls += 1

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    global function_calls
    function_calls = 0  # 호출 횟수 초기화
    result = recursion(s, 0, len(s) - 1)
    return result, function_calls


for _ in range(int(input())):
    temp_str = input().rstrip()
    result, function_calls = isPalindrome(temp_str)
    print(result, function_calls)
