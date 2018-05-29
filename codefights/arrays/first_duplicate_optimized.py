def firstDuplicate(a):
    seen = {}

    for val in a:
        if val in seen:
            return val
        seen[val] = True

    return -1

test1 = [2, 1, 3, 5, 3, 2]
print(firstDuplicate(test1))
test2 = [2, 4, 3, 5, 1]
print(firstDuplicate(test2))