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
    bits = ''.join(f"{ord(c):08b}" for c in message)
    bit_index = 0

    available_slots = sum(1 for cell in flat_grid if cell != 0)
    if available_slots < len(bits):
        raise ValueError("Not enough space in the Sudoku grid to encode the message.")

    for i in range(len(flat_grid)):
        if flat_grid[i] != 0 and bit_index < len(bits):
            flat_grid[i] = (flat_grid[i] & ~1) | int(bits[bit_index])
            bit_index += 1

    return [flat_grid[i:i+9] for i in range(0, 81, 9)]

