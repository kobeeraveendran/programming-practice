def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0

    for i in range(1, len(inputArray)):
        curr_diff = abs(inputArray[i] - inputArray[i - 1])
        if curr_diff > max_diff:
            max_diff = curr_diff

    return max_diff