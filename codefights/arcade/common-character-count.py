# Kobee Raveendran
# Common Character Count - CodeFights

# Given two strings, find the number of common characters between them

def commonCharacterCount(s1, s2):
    string1 = list(s1)
    string2 = list(s2)

    if len(s1) < len(s2):
        shorterString = string1
        longerString = string2
    else:
        shorterString = string2
        longerString = string1

    endIndex = min(len(s1), len(s2))
    count = 0

    for i in range(endIndex):
        if shorterString[i] in longerString:
            count += 1
            longerString.remove(shorterString[i])

    return count

print(commonCharacterCount('abca', 'xyzbac'))