import random

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_start = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_start[0] + i][box_start[1] + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in random.sample(range(1, 10), 9):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku(empty_cells=40):
    board = [[0] * 9 for _ in range(9)]
    solve(board)

    count = 0
    while count < empty_cells:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count += 1
    return board

def encode_message_in_sudoku(grid, message):
    flat_grid = sum(grid, [])
    msg_index = 0
    encoded_digits = [(ord(c) % 9) + 1 for c in message]

    for i in range(len(flat_grid)):
        if flat_grid[i] == 0 and msg_index < len(encoded_digits):
            flat_grid[i] = encoded_digits[msg_index]
            msg_index += 1

    encoded_grid = [flat_grid[i:i + 9] for i in range(0, 81, 9)]
    return encoded_grid
