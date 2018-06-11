def firstNotRepeatingCharacter(s):
    index_track = {}

    for i in range(len(s)):
        if s[i] in index_track:
            index_track[s[i]] = -1
        else:
            index_track[s[i]] = i

    min_index = len(s)
    retval = '_'

    for key in index_track:
        if index_track[key] > -1:
            min_index = min(index_track[key], min_index)
            retval = s[min_index]
    
    return retval