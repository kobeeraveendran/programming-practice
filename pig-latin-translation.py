def translate_to_pig(english):
    stringlist = english.split(' ')

    newstringlist = []

    wordcount = 0
    for string in stringlist:
        templist = list(string)
        tempchar = templist[0]
        templist.append(tempchar.lower())
        templist.remove(tempchar)
        if wordcount == 0:
            templist[0] = templist[0].upper()
            wordcount += 1
        templist.append('ay')
        newstringlist.append(''.join(templist))
        newstringlist.append(' ')

    retval = ''.join(newstringlist)

    return retval

def translate_to_eng(piglatin):
    stringlist = piglatin.split(' ')

print("Translate 'The quick brown fox' to Pig Latin: " + translate_to_pig('The quick brown fox'))