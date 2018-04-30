def reverse_list(input):
    size = len(input)
    strFlag = False

    if(isinstance(input, str)):
        input = list(input)
        strFlag = True

    for i in range(size // 2):
        temp = input[size - i - 1]
        input[size - i - 1] = input[i]
        input[i] = temp

    if strFlag:
        return ''.join(input)

    return input

list1 = [3, 5, 7, 9]
list2 = 'test with strings'

print("Reversed list: " + str(reverse_list(list1)))
print("Reversed list 2: " + str(reverse_list(list2)))