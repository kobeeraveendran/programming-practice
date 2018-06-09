def chessKnight(cell):
    col = ord(cell[0]) - 96
    row = eval(cell[1])
    num_moves = 0

    num_moves += 1 if row + 2 <= 8 and col + 1 <= 8 else 0
    num_moves += 1 if row + 1 <= 8 and col + 2 <= 8 else 0
    num_moves += 1 if row - 1 >= 1 and col + 2 <= 8 else 0
    num_moves += 1 if row - 2 >= 1 and col + 1 <= 8 else 0
    num_moves += 1 if row - 1 >= 1 and col - 2 >= 1 else 0
    num_moves += 1 if row - 2 >= 1 and col - 1 >= 1 else 0
    num_moves += 1 if row + 2 <= 8 and col - 1 >= 1 else 0
    num_moves += 1 if row + 1 <= 8 and col - 2 >= 1 else 0

    return num_moves