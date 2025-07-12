def decode_message_from_sudoku(grid, message_length):
    flat_grid = sum(grid, [])
    bits_needed = message_length * 8
    bits = []

    for val in flat_grid:
        if val != 0 and len(bits) < bits_needed:
            bits.append(str(val & 1))

    if len(bits) < bits_needed:
        raise ValueError("Grid does not contain enough data to decode the full message.")

    chars = [chr(int(''.join(bits[i:i+8]), 2)) for i in range(0, bits_needed, 8)]
    return ''.join(chars)
