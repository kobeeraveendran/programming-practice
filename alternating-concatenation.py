# Kobee Raveendran
# April 27, 2018
# Alternating concatenation of two lists in python

def combine_lists(list1, list2):
    new_list = []
    maxlen = 0

    # determine lengths
    if len(list1) == len(list2):
        maxlen = len(list1)
    elif len(list1) < len(list2):
        maxlen = len(list2)
    else:
        maxlen = len(list1)

    for i in range(maxlen):
        if i >= len(list1):
            new_list.append(list2[i])
        elif i >= len(list2):
            new_list.append(list1[i])
        else:
            new_list.append(list1[i])
            new_list.append(list2[i])
        
    return new_list

basic_list1 = ['a', 'b', 'c', 'd']
basic_list2 = [1, 2, 3, 4, 5, 6]

print("Concatenated list: " + str(combine_lists(basic_list1, basic_list2)))