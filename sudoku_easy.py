import os
import pandas as pd

os.chdir("/Users/alicesmail/Desktop")


def zeros_exist(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return True
    return False


def is_zero(sudoku, row, col):
    if sudoku[row][col] == 0:
        return True
    else:
        return False


def check_number(sudoku, number, zero_row, zero_col):
    for col in range(9):
        if sudoku[zero_row][col] == number and col != zero_col:
            return False

    for row in range(9):
        if sudoku[row][zero_col] == number and row != zero_row:
            return False

    if zero_col in [0, 1, 2]:
        if zero_row in [0, 1, 2]:
            for col in range(3):
                for row in range(3):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False
        if zero_row in [3, 4, 5]:
            for col in range(3):
                for row in range(3, 6):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False
        if zero_row in [6, 7, 8]:
            for col in range(3):
                for row in range(6, 9):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False

    if zero_col in [3, 4, 5]:
        if zero_row in [0, 1, 2]:
            for col in range(3, 6):
                for row in range(3):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False
        if zero_row in [3, 4, 5]:
            for col in range(3, 6):
                for row in range(3, 6):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False
        if zero_row in [6, 7, 8]:
            for col in range(3, 6):
                for row in range(6, 9):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False

    if zero_col in [6, 7, 8]:
        if zero_row in [0, 1, 2]:
            for col in range(6, 9):
                for row in range(3):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False
        if zero_row in [3, 4, 5]:
            for col in range(6, 9):
                for row in range(3, 6):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False
        if zero_row in [6, 7, 8]:
            for col in range(6, 9):
                for row in range(6, 9):
                    if sudoku[row][col] == number and zero_row != row and zero_col != col:
                        return False
    return True


def solve(sudoku, row, col):
    while zeros_exist(sudoku):
        print("zeros exist")
        for row in range(9):
            for col in range(9):
                if is_zero(sudoku, row, col):
                    print(f"{row, col} is zero")
                    possibilities = []
                    for num in range(1,10):
                        if check_number(sudoku, num, row, col):
                            possibilities.append(num)
                    print(f"All possibilities for {row, col}: {possibilities}")
                    if len(possibilities) == 1:
                        sudoku[row][col] = possibilities[0]
                        print(sudoku)
                        print("\n")
                    else:
                        sudoku[row][col] = 0
    else:
        print("no more zeros")
        return False


sudoku_to_solve = pd.read_csv("sudoku_to_solve.csv", header=None)
print(sudoku_to_solve)
print("\n")
print(solve(sudoku_to_solve, 0, 0))




