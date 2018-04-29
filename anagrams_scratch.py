def anagrams(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    if len(string1) != len(string2):
        return False

    countFlag = True

    charFreqs1 = [0] * 26
    charFreqs2 = [0] * 26

    for i in range(len(string1)):
        # ord() will get the ASCII value of the character
        charFreqs1[ord(string1[i]) - ord('a')] += 1
        charFreqs2[ord(string2[i]) - ord('a')] += 1

    for i in range(26):
        if charFreqs1[i] != charFreqs2[i]:
            countFlag = False

    return countFlag

# testing
print("Clint Eastwood and Old West Action: " + str(anagrams("Clint Eastwood", "Old West Action")))
print("Dog and God: " + str(anagrams("dog", "God")))
print("Racecar and racecars: " + str(anagrams("racecar", "racecars")))
print("Scars and racks: " + str(anagrams("scars", "racks")))