import itertools

def stringsRearrangement(inputArray):
    string_perms = itertools.permutations(inputArray)

    for permutation in string_perms:
        match = True

        for i in range(len(permutation) - 1):
            if not differsByOne(permutation[i], permutation[i + 1]):
                match = False
                break

        if match:
            return match
    
    return False


def differsByOne(string1, string2):
    count = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
        
        if count > 1:
            return False

    return count == 1