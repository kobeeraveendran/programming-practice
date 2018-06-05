def avoidObstacles(inputArray):
    # start with the longest consecutive
    # subsequence length + 1

    inputArray.sort()

    # the shortest consecutive subsequence is 1
    lcss = 1

    # find the longest consecutive subsequence
    for i in range(1, len(inputArray)):
        if inputArray[i] == inputArray[i - 1] + 1:
            lcss += 1
        else:
            lcss = 1

    # since the step size must be AT LEAST
    # LCSS + 1, start there
    lcss += 1

    return minimum_step(inputArray, lcss)
    
# recursive fn to determine the step size if the
# LCSS is not long enough
def minimum_step(inputArray, step):
    min_step = step
    for i in range(len(inputArray)):
        if inputArray[i] % step == 0:
            min_step = minimum_step(inputArray, step + 1)
    
    return min_step