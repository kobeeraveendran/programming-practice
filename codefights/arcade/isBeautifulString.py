import numpy as np

def isBeautifulString(inputString):    
    letters = np.zeros(26, dtype = int)

    for i in range(len(inputString)):
        letters[ord(inputString[i]) - 97] += 1

    for i in range(1, len(letters)):
        if letters[i] > letters[i - 1]:
            return False

    return True
