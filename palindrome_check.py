def isPalindrome(inputstring):
    # accepts strings with spaces, punctuation, and varying case
    inputstring = inputstring.replace(' ', '').replace(',', '').replace('.', '').lower()

    size = len(inputstring)
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
print("Palindrome? - A but tuba: " + str(isPalindrome('A but tuba.')))
print("Palindrome? - A car, a man, a maraca: " + str(isPalindrome('A car, a man, a maraca')))