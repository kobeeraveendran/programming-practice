def arrayChange(inputArray):
    num_moves = 0

    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            num_moves += inputArray[i - 1] - inputArray[i] + 1
            inputArray[i] += inputArray[i - 1] - inputArray[i] + 1

    return num_moves