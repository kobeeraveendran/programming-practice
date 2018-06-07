import numpy as np

def minesweeper(matrix):

    new_board = np.zeros((len(matrix), len(matrix[0])), dtype = int)

    board_height = len(matrix[0])
    board_width = len(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            mine_count = 0
            # top
            if j < board_height - 1:
                mine_count += 1 if matrix[i][j + 1] else 0          
            
            # right
            if i < board_width - 1:
                mine_count += 1 if matrix[i + 1][j] else 0   

            # left
            if i > 0:
                mine_count += 1 if matrix[i - 1][j] else 0    
            
            # bottom
            if j > 0:
                mine_count += 1 if matrix[i][j - 1] else 0    
            
            # diagonals
            if i < board_width - 1 and j < board_height - 1:
                mine_count += 1 if matrix[i + 1][j + 1] else 0                

            if i < board_width - 1 and j > 0:
                mine_count += 1 if matrix[i + 1][j - 1] else 0               

            if i > 0 and j < board_height - 1:
                mine_count += 1 if matrix[i - 1][j + 1] else 0                

            if i > 0 and j > 0:
                mine_count += 1 if matrix[i - 1][j - 1] else 0

            new_board[i][j] = mine_count       

    return new_board

test1 = [[True, False, False],
         [False, True, False],
         [False, False, False]]

test2 = [[False, False, False],
         [False, False, False]]

test3 = [[True, False, False, True], 
         [False, False, True, False], 
         [True, True, False, True]]

test4 = [[True, False], 
         [False, False]]

test5 = [[True, True, True, True, True], 
         [False, False, False, False, False]]

test6 = [[True, False, False, False, False], 
         [False, False, False, False, False], 
         [False, False, False, False, False]]

test7 = [[False, False, False, False], 
         [False, True, False, False], 
         [False, False, False, False]]

test8 = [[True, True], 
         [False, False], 
         [True, True], 
         [False, False]]

test9 = [[True, True], 
         [True, True]]



print(minesweeper(test1))
print(minesweeper(test2))
print(minesweeper(test3))
print(minesweeper(test4))
print(minesweeper(test5))
print(minesweeper(test6))
print(minesweeper(test7))
print(minesweeper(test8))
print(minesweeper(test9))
