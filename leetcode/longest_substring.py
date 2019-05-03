def lengthOfLongestSubstring(s: str) -> int:
        
    if len(s) == 0 or len(s) == 1:
        return len(s)
    
    maxlen = 0
    substr = ''
    
    for i in range(len(s)):
        if s[i] not in substr:
            substr += s[i]
            
        else:
            cutoff = substr.index(s[i])
            substr = substr[cutoff + 1:]
            substr += s[i]
            
        maxlen = max(maxlen, len(substr))

        print(substr)
    
    return maxlen

test1 = 'pwwkew'

print(lengthOfLongestSubstring(test1))