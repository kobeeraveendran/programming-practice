def missingNumber(numberList, maxRange):

    n = maxRange - 1

    expected = n * (n + 1) / 2

    actual = sum(numberList)
    #print('expected sum: ' + str(expected))
    #print('actual sum: ' + str(actual))

    return expected - actual

def sum(numList):

    total = 0

    for num in numList:
        total += num

    return total

# test cases
tc1 = [x for x in range(1, 100) if x != 57]

print(missingNumber(tc1, 100))

tc2 = [x for x in range(1, 100) if x != 20]
print(missingNumber(tc2, 100))

tc3 = [x for x in range(1, 200) if x != 109]
print(missingNumber(tc3, 200))