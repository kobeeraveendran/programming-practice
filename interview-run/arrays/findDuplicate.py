def findDuplicate(array, n):

    total = n * (n + 1) / 2

    array_total = 0

    for num in array:
        array_total += num

    return int(array_total - total)

tc1 = [1, 2, 3, 4, 4]
tc2 = [1, 2, 3, 4, 2]

print(findDuplicate(tc1, 4))
print(findDuplicate(tc2, 4))

def findDuplicateGeneral(array):

    seen = set()

    for num in array:
        if num in seen:
            return num

        else:
            seen.add(num)

print(findDuplicateGeneral(tc1))
print(findDuplicateGeneral(tc2))