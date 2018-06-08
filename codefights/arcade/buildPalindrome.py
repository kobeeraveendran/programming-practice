def buildPalindrome(st):
    if checkIfPalindrome(st):
        return st

    # go through st and append substrings of st
    # (from small to large) and check if it's a palindrome
    for i in range(len(st)):
        if(checkIfPalindrome(st + st[i - len(st)::-1])):
            return st + st[i - len(st)::-1]

def checkIfPalindrome(st):
    return st == st[::-1]