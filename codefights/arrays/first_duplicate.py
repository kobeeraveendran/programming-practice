# Kobee Raveendran
# CodeFights - Arrays - firstDuplicate
# find the first duplicate s.t. the second occurrence
# comes before the second occurrences of all other duplicates
# in the array

def firstDuplicate(a):
    seen = {}
    indexCompare = {}

    for num in a:
        if num in seen:
            seen[num] += 1

        else:
            seen[num] = 1
        
    for key in seen:
        if seen[key] > 1:
            a.remove(key)
            indexCompare[key] = a.index(key)

    minIndex = len(a) + 2
    retval = 0

    for key in indexCompare:
        if indexCompare[key] < minIndex:
            minIndex = indexCompare[key]
            retval = key

    if retval == 0:
        return -1
    else:
        return retval


testList = [2, 1, 3, 5, 3, 2]

print(firstDuplicate(testList))