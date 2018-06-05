def areSimilar(a, b):

    if str(a) == str(b):
        return True

    a_diff = []
    b_diff = []

    for i in range(len(a)):
        if a[i] != b[i]:
            a_diff.append(a[i])
            b_diff.append(b[i])
    
    if len(a_diff) > 2:
        return False

    a_diff.reverse()

    return str(a_diff) == str(b_diff)

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