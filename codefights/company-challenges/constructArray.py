def constructArray(size):
    retval = []
    temp_i = 1
    temp_size = size

    for i in range(size):
        if i % 2 == 0:
            retval.append(temp_i)
            temp_i += 1
        else:
            retval.append(temp_size)
            temp_size -= 1

    return retval