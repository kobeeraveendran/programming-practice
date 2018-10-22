def anagramCheck(string1, string2):

    return sorted(string1) == sorted(string2)

print(anagramCheck('army', 'mary'))