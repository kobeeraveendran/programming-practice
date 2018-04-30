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

    newstringlist = []

    first = True
    for string in stringlist:
        templist = list(string)
        del templist[len(templist) - 1]
        del templist[len(templist) - 1]
        tempchar = templist[len(templist) - 1]
        templist.remove(tempchar)
        if first:
            templist.insert(0, tempchar.upper())
            templist[1] = templist[1].lower()
            first = False
        else:
            templist.insert(0, tempchar)
        newstringlist.append(''.join(templist))
        newstringlist.append(' ')

    retval = ''.join(newstringlist)

    return retval


print("Translate 'The quick brown fox' to Pig Latin: " + translate_to_pig('The quick brown fox'))

print("Translate 'Hetay uickqay rownbay oxfay' to English: " + translate_to_eng('Hetay uickqay rownbay oxfay'))