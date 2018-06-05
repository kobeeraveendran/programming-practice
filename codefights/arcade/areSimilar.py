def areSimilar(a, b):
    if len(a) != len(b):
        return False

    if str(a) == str(b):
        return True

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            a = swap(a, i, j)

            if str(a) == str(b):
                return True

            a = swap(a, j, i)

    return False

def swap(a, first, second):
    temp = a[first]
    a[first] = a[second]
    a[second] = temp

    return a

test1a = [1, 2, 3]
test1b = [1, 2, 3]

test2a = [1, 2, 3]
test2b = [2, 1, 3]

test3a = [1, 2, 2]
test3b = [2, 1, 1]

test4a = [4, 6, 3]
test4b = [3, 4, 6]

print('Test 1: Expected: True' + ' Output: ' + str(areSimilar(test1a, test1b)))
print('Test 2: Expected: True' + ' Output: ' + str(areSimilar(test2a, test2b)))
print('Test 3: Expected: False' + ' Output: ' + str(areSimilar(test3a, test3b)))
print('Test 4: Expected: False' + ' Output: ' + str(areSimilar(test4a, test4b)))