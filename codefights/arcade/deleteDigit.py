def deleteDigit(n):
    # find the minimum digit and remove the first instance of it
    digits = list(str(n))
    digits.remove(min(digits))

    return eval(''.join(digits))