import numpy as np

def minesweeper(matrix):

    new_board = np.zeros((len(matrix), len(matrix[0])), dtype = int)
    matrix = np.array(matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                matrix[row][col] = 1
                new_board[row][col] = 1
            else:
                matrix[row][col] = 0

    print(new_board)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                # top left corner
                if row == 0 and col == 0:
                    new_board[row][col] = sum(matrix[row + 1][col:col + 2]) + matrix[row][col + 1]
                    
                # bottom right corner
                elif row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                    new_board[row][col] = sum(matrix[row - 1][col - 1:]) + matrix[row][col - 1]
                    
                # top right corner
                elif col == len(matrix[0]) - 1 and row == 0:
                    new_board[row][col] = sum(matrix[row + 1][col - 1:]) + matrix[row][col - 1]
                
                # bottom left corner
                elif row == len(matrix) - 1 and col == 0:
                    new_board[row][col] = sum(matrix[row - 1][:col + 2]) + matrix[row][col + 1]
                    
                # non-corner border tiles
                
                # left side
                elif col == 0:
                    new_board[row][col] = sum(matrix[row - 1:row + 2][col + 1]) + matrix[row - 1][col] + matrix[row + 1][col]
                
                # top side
                elif row == 0:
                    new_board[row][col] = sum(matrix[row + 1][col - 1:col + 2]) + matrix[row][col - 1] + matrix[row][col + 1]

                # right side
                elif col == len(matrix[0]) - 1:
                    new_board[row][col] = sum(matrix[row - 1:row + 2][col - 1]) + matrix[row - 1][col] + matrix[row + 1][col]

                # bottom side
                elif row == len(matrix) - 1:
                    new_board[row][col] = sum(matrix[row - 1][col - 1:col + 2]) + matrix[row][col - 1] + matrix[row][col + 1]
                    
                # general case (inner tiles)
                else:
                    row1 = sum(matrix[row - 1][col - 1:col + 2])
                    row2 = matrix[row][col - 1] + matrix[row][col + 1]
                    row3 = sum(matrix[row + 1][col - 1:col + 2])
                    new_board[row][col] = sum([row1, row2, row3])

    return new_board

test1 = [[True, False, False],
         [False, True, False],
         [False, False, False]]

test2 = [[False, False, False],
         [False, False, False]]

test3 = [[True, False, False, True], 
         [False, False, True, False], 
         [True, True, False, True]]

print(minesweeper(test1))
print(minesweeper(test2))
print(minesweeper(test3))