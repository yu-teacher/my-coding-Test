num = int(input())
numbers = list(map(int, input().split()))
operators_count = list(map(int, input().split()))

operationResults = []

def backtrack(index, current_result):
    if index == num - 1:
        operationResults.append(current_result)
        return
    
    if operators_count[0] > 0:
        operators_count[0] -= 1
        backtrack(index + 1, current_result + numbers[index + 1])
        operators_count[0] += 1
    
    if operators_count[1] > 0:
        operators_count[1] -= 1
        backtrack(index + 1, current_result - numbers[index + 1])
        operators_count[1] += 1
    
    if operators_count[2] > 0:
        operators_count[2] -= 1
        backtrack(index + 1, current_result * numbers[index + 1])
        operators_count[2] += 1
    
    if operators_count[3] > 0:
        operators_count[3] -= 1
        backtrack(index + 1, int(current_result / numbers[index + 1]))
        operators_count[3] += 1

backtrack(0, numbers[0])

print(max(operationResults))  # 최댓값 출력
print(min(operationResults))  # 최솟값 출력