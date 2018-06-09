import string

def isMAC48Address(inputString):
    split_string = inputString.split('-')
    filter(None, split_string)

    if len(split_string) != 6:
        return  False

    for str in split_string:
        if len(str) != 2:
            return False
        for j in range(2):
            if not (str[j].isdigit() or str[j] in string.ascii_uppercase[:6]):
                return False
            
    return True