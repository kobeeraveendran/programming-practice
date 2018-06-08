def isBeautifulString(inputString):
    freqs = [inputString.count(i) for i in string.ascii_lowercase]

    return freqs[::-1] == sorted(freqs)