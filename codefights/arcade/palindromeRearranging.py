def palindromeRearranging(inputString):
    lettercount = {}

    charList = list(inputString)

    for char in charList:
        if char in lettercount:
            lettercount[char] += 1
        else:
            lettercount[char] = 1

    stringlen = len(inputString)
    center_candidates = 0

    for key in lettercount:
        if lettercount[key] % 2 != 0:
            center_candidates += 1

    if stringlen % 2 != 0 and center_candidates > 1:
        return False
    elif stringlen % 2 == 0 and center_candidates > 0:
        return False
        
    return True