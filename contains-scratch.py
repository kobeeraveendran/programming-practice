def contains(target, list):
    for element in list:
        if element == target:
            return True
    
    return False

list1 = [1, 3, 6, 7, 9]
list2 = ['cat', 'dog', 'hamburger', 'cheese']
list3 = ['car', 'airplane', 'train']

print("List1 contains 6? " + str(contains(6, list1)))
print("List2 contains squirrel? " + str(contains('squirrel', list2)))
print("List3 contains airplane? " + str(contains('airplane', list3)))