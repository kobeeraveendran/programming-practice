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