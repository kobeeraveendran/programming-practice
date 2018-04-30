def isPalindrome(inputstring):
    size = len(inputstring)

    # accepts strings with spaces or varying case
    inputstring = inputstring.replace(' ', '').lower()

    tempstring = inputstring
    inputstring = list(inputstring)

    for i in range(size // 2):
        temp = inputstring[i]
        inputstring[i] = inputstring[size - i - 1]
        inputstring[size - i - 1] = temp

    inputstring = ''.join(inputstring)

    return tempstring == inputstring

print("Palindrome? - racecar: " + str(isPalindrome('racecar')))
print("Palindrome? - cheese: " + str(isPalindrome('cheese')))