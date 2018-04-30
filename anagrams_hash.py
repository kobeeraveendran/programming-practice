def anagrams(string1, string2):
    string1 = string1.replace(' ', '').lower()
    string2 = string2.replace(' ', '').lower()

    count1 = {}
    count2 = {}

    if len(string1) != len(string2):
        return False

    for letter in string1:
        if letter in count1:
            count1[letter] += 1

        else:
            count1[letter] = 1
        
    for letter in string2:
        if letter in count2:
            count2[letter] += 1

        else:
            count2[letter] = 1

    for letter in string1:
        if count1[letter] != count2[letter]:
            return False

    return True

print("Clint Eastwood and Old West Action: " + str(anagrams("Clint Eastwood", "Old West Action")))
print("Dog and God: " + str(anagrams("dog", "god")))
print("Racecars and racecar: " + str(anagrams("Racecars", "racecar")))
print("Scars and racks: " + str(anagrams("scars", "racks")))