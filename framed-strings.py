def frame_string(string):
    stringlist = string.split(' ')

    framelength = 0

    for string in stringlist:
        if len(string) > framelength:
            framelength = len(string)

    framelength += 4

    print('*' * framelength)

    for string in stringlist:
        print('* ' + string + ' ' * (framelength - len(string) - 3) + '*')

    print('*' * framelength)
    
frame_string("Hello World in a frame")
print('')
frame_string("Waaaaaaaaaay longer string to test borders")