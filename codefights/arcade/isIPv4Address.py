def isIPv4Address(inputString):
    # split by decimals
    decomposed_address = inputString.split('.')

    # check if non-digits are present
    for elem in decomposed_address:
        if not elem.isdigit():
            return False
        
    # this means there are more or less dots than necessary, 
    # or more or less numbers than necessary
    if len(decomposed_address) != 4:
        return False

    # convert list of strings to list of ints
    decomposed_address = [int(x) for x in decomposed_address]

    for i in range(len(decomposed_address)):
        if 0 > decomposed_address[i] or 255 < decomposed_address[i]:
            return False

    return True
    