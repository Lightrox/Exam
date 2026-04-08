N = 8

def solve(board, row=0):
    if row == N:
        for r in board:
            print(" ".join("Q" if c else "." for c in r))
        print()
        return

    for col in range(N):

        # Check column
        if any(board[i][col] for i in range(row)):
            continue

        # Check upper-left diagonal
        if any(board[i][j] for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1))):
            continue

        # Check upper-right diagonal
        if any(board[i][j] for i, j in zip(range(row-1, -1, -1), range(col+1, N))):
            continue

        # Place queen
        board[row][col] = 1

        # Recurse
        solve(board, row + 1)

        # Backtrack
        board[row][col] = 0


# Initialize board
board = [[0]*N for _ in range(N)]
solve(board)