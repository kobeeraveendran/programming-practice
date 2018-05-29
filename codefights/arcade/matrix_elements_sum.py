# Kobee Raveendran
# Matrix Elements Sum - CodeFights
# given a 2D matrix (where each entry is a 'room' with a price), 
# find the total cost of all valid rooms. Rooms that have a cost of
# 0 (free) and all rooms below that room are invalid.

import numpy as np

def matrixElementsSum(matrix):
    sum = 0

    newMatrix = np.array(matrix)
    newMatrix = np.transpose(newMatrix)

    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[i])):
            if newMatrix[i][j] != 0:
                sum += newMatrix[i][j]
            else:
                break
    
    return sum