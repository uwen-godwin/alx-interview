#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, results):
    """Use backtracking to find all solutions"""
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        results.append(solution)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1, results) or res
            board[i][col] = 0

    return res

def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    results = []
    solve_nqueens_util(board, 0, results)
    return results

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in sorted(solutions):
        print(solution)

if __name__ == "__main__":
    main()
