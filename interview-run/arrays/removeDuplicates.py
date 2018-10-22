def removeDuplicates(array):

    return list(dict.fromkeys(array))

test1 = [1, 1, 2, 1, 4, 2, 3, 6, 7, 1]

print('New list without duplicates: ' + str(removeDuplicates(test1)))