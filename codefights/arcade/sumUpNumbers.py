import re

def sumUpNumbers(inputString):
    parsed = re.findall('\d+', inputString)

    return sum(map(int, parsed))