# The 8 Queens Problem:
# Place 8 queens on an 8x8 chessboard such that:
# a. Each row has exactly one queen
# b. Each column has exactly one queen
# c. No two queens attack each other (i.e., no same row, column, or diagonal)

# Function to check if a queen can be safely placed at board[row][col]
def is_safe(board, row, col):
    for i in range(row):
        # a & b. Check for another queen in the same column
        if board[i] == col:
            return False
        # c. Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

# Recursive function to place queens row by row
def solve_queens(board, row):
    # Base case: all 8 queens placed successfully
    if row == 8:
        print_board(board)
        return True  # Change to False here if you want to find all solutions
    # Try placing queen in each column of the current row
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col  # Place queen
            if solve_queens(board, row + 1):
                return True  # Stop after first valid solution
    return False  # No valid column in this row, backtrack

# Function to print the board in a readable format
def print_board(board):
    print("\n8 Queens Solution:")
    for row in range(8):
        line = ["." for _ in range(8)]  # Empty board row
        line[board[row]] = "Q"          # Place queen
        print(" ".join(line))           # Print row

# Initialize the board with -1 (no queens placed)
board = [-1] * 8

# Start solving from the first row
solve_queens(board, 0)
