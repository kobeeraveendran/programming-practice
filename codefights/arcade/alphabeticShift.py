def alphabeticShift(inputString):
    inputString = list(inputString)

    for i in range(len(inputString)):
        print(inputString[i])
        inputString[i] = chr((ord(inputString[i]) + 1)) if inputString[i] != 'z' else 'a'

    return ''.join(inputString)

print(alphabeticShift('crazy'))