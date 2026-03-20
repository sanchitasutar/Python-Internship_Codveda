def is_safe(board, row, col, n):
    # check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row+1, n)
            board[row][col] = 0  # backtrack


def print_board(board, n):
    print("\nSolution:")
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else ".", end=" ")
        print()


n = int(input("Enter number of queens: "))
board = [[0]*n for _ in range(n)]

solve_nqueens(board, 0, n)
