def find_max(inputlist):
    # sorting way
    size = len(inputlist)
    inputlist.sort()
    return inputlist[size - 1]

list1 = [3, 6, 2, 9, 5]
print("Largest of [3, 6, 2, 9, 5]: " + str(find_max(list1)))

# with strings too!
list2 = ['apple', 'cat', 'barbeque']
print("Largest of [apple, cat, barbeque]: " + str(find_max(list2)))