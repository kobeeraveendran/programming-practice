def zigzag(list):
    zigzag = True
    # 0 if next is less, 1 if next is greater
    toggle = 0

    if len(list) == 1:
        return True

    if list[0] > list[1]:
        toggle = 0
    elif list[0] < list[1]:
        toggle = 1
    else:
        return False

    #if greater:
    for i in range(1, len(list)):
        if toggle == 0:
            if list[i] < list[i - 1]:
                toggle = 1
            elif list[i] > list[i - 1]:
                return False
            else:
                return False
        else:
            if list[i] > list[i - 1]:
                toggle = 0
            elif list[i] < list[i - 1]:
                return False
            else:
                return False
    
    return zigzag


test1 = [4, 2, 3, 1, 5, 3]
test2 = [7, 3, 5, 5, 2]
test3 = [3, 8, 6, 4, 5]
test4 = [1]

print(zigzag(test1))
print(zigzag(test2))
print(zigzag(test3))
print(zigzag(test4))