def is_valid(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + startRow][j + startCol] == num:
                return False
    return True

def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))

if solve_sudoku(sudoku):
    for row in sudoku:
        print(' '.join(map(str, row)))