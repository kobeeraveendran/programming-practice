def findRotations(array):

    min_value = 1e7
    min_index = 0

    for i in range(len(array)):

        if array[i] < min_value:
            min_value = array[i]
            min_index = i

    return min_index

    '''
    low = 0
    high = len(array) - 1
    curr_min = int(1e7)
    min_index = -1

    while low <= high:

        if array[low] <= curr_min:
            curr_min = array[low]
            minIndex = low
            array[low] += 1

        elif array[high] <= curr_min:
            curr_min = array[high]
            minIndex = high
            high -= 1

    return minIndex
    '''

test1 = [8, 9, 10, 2, 5, 6]

print(findRotations(test1))