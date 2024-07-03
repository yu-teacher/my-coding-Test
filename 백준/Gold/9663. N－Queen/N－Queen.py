import sys
input = sys.stdin.readline  

n = int(input())

def is_attacked(current_col):
    for previous_col in range(current_col): 
        if queens[current_col] == queens[previous_col] or abs(queens[current_col] - queens[previous_col]) == abs(current_col - previous_col):
            return True
    return False

def solve_queens(row):
    global solution_count  

    if row == n:
        solution_count += 1  
    else:
        for col in range(n):  
            queens[row] = col  
            if not is_attacked(row):  
                solve_queens(row + 1)  

queens = [0] * n  
solution_count = 0 
solve_queens(0)  

print(solution_count)