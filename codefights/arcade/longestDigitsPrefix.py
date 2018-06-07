def longestDigitsPrefix(inputString):
    digitlist = []

    for i in range(len(inputString)):
        if not inputString[i].isdigit():
            break
        digitlist.append(inputString[i])

    return ''.join(digitlist)