import re

def sumUpNumbers(inputString):
    parsed = re.findall('\d+', inputString)

    return 0 if len(parsed) == 0 else sum(map(int, parsed))