def firstNotRepeatingCharacter(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
    
    return '_'