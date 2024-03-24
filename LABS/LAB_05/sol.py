def is_safe(board, row, col, N):
    # iterates over each column and checks if there is another queen 
    # in the same row and column
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def count_and_print_n_queens_solutions_util(board, col, N, count):
    if col >= N:
        # Print the board when a solution is found
        print_board(board)
        print()
        count[0] += 1
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            count_and_print_n_queens_solutions_util(board, col + 1, N, count)
            board[i][col] = 0

def count_and_print_n_queens_solutions(N):
    board = [[0] * N for _ in range(N)]
    count = [0]  # Using a list to pass as reference, so its value can be modified inside the function

    count_and_print_n_queens_solutions_util(board, 0, N, count)
    return count[0]

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))


# main code
N = int(input("Enter dimension of chess-board: "))
print("Number of solutions for an", N, "x", N, "board:", count_and_print_n_queens_solutions(N))
