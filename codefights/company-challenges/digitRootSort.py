import operator

def digitRootSort(numbers):

    tuple_list = []
    # find sum of digits
    for i in range(len(numbers)):
        temp_sum = 0
        as_str = str(numbers[i])
        for j in range(len(as_str)):
            temp_sum += int(as_str[j])

        tuple_list.append((numbers[i], temp_sum))

    tuple_list.sort(key = operator.itemgetter(1, 0))

    retval = []
    for i in range(len(tuple_list)):
        retval.append(tuple_list[i][0])

    return retval