def newNumeralSystem(number):
    target = ord(number) - 65
    retval = []

    for i in range(target // 2 + 1):
        retval.append(str(chr(i + 65)) + " + " + str(chr(target - i + 65)))

    return retval