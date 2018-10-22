def binaryArraySort(array):

    zero_count = 0
    one_count = 0

    for num in array:
        if num == 0:
            zero_count += 1

        else:
            one_count += 1

    for i in range(len(array)):
        if i < zero_count:
            array[i] = 0

        else:
            array[i] = 1

    return array

tc1 = [1, 0, 1, 0, 1, 0, 0, 1]

print(binaryArraySort(tc1))