def palindromeRearranging(inputString):
    lettercount = {}

    charList = list(inputString)

    for char in charList:
        if char in lettercount:
            lettercount[char] += 1
        else:
            lettercount[char] = 1

    stringlen = len(inputString)
    centerflag = 0

    for key in lettercount:
        if lettercount[key] % 2 != 0:
            if stringlen % 2 != 0 and centerflag == 1:
                return False
            elif stringlen % 2 == 0:
                return False
            else:
                centerflag == 1
    
    return True