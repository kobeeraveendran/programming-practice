def missingNumberImprovedNaive(numberList, maxRange):

    #numberList.sort()

    missing = []

    for i in range(1, maxRange):
        if i in numberList:
            continue

        else:
            missing.append(i)

    return missing

def missingNumberImprovedBetter(numberList, maxRange):

    maxRange -= 1

    numberList.sort()

    missing = []

    i = 1
    j = 0

    while i != maxRange:
        if numberList[j] != i:
            i += 1
            missing.append(numberList[j] - 1)

        i += 1
        j += 1

    return missing


tc1 = [x for x in range(1, 100)]
tc1.remove(57)
tc1.remove(25)

print(missingNumberImprovedBetter(tc1, 100))

tc2 = [x for x in range(1, 100)]
tc2.remove(52)
tc2.remove(89)
print(missingNumberImprovedBetter(tc2, 100))

tc3 = [x for x in range(1, 200) if x != 109 or x != 21]
tc3.remove(109)
tc3.remove(21)
print(missingNumberImprovedBetter(tc3, 200))