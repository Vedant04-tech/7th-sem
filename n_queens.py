"""Solve the N-Queens puzzle using backtracking."""

n = int(input("Enter value of N: "))
if n <= 0:
    raise ValueError("N must be greater than zero.")

# 0 means empty; 1 means a queen is placed in that cell.
board = [[0 for _ in range(n)] for _ in range(n)]


def is_safe(row, col):
    """Return True if no earlier queen can attack this position."""
    # Check the same column above the current row.
    for r in range(row):
        if board[r][col] == 1:
            return False

    # Check the upper-left diagonal.
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check the upper-right diagonal.
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    return True


def solve(row):
    # If every row has a queen, a solution has been found.
    if row == n:
        return True

    # Try placing a queen in each column of this row.
    for col in range(n):
        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            # This position led to a dead end, so undo the choice.
            board[row][col] = 0

    return False


if solve(0):
    print("\nN-Queens solution:")
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
else:
    print("No solution exists for this value of N.")
