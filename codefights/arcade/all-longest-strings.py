# Kobee Raveendran
# All Longest Strings - CodeFights

# given an array of strings, return another array
# containing all of its longest strings

def allLongestStrings(inputArray):

    maxLen = -1
    longestStrings = []

    # find length of the largest string(s)
    for string in inputArray:
        if len(string) > maxLen:
            maxLen = len(string)

    for string in inputArray:
        if len(string) == maxLen:
            longestStrings.append(string)

    return longestStrings