def zeroSumSubArray(arr):

    seen = set()
    seen.add(0)

    total = 0

    for i in range(len(arr)):
        total += arr[i]

        if total in seen:
            return True

        seen.add(total)

    return False

tc1 = [4, -6, 3, -1, 4, 2, 7]
tc2 = [4, 2, -3, -1, 0, 4]

print("Zero sum subarray exists") if zeroSumSubArray(tc1) else print("Zero sum subarray does not exist")


# print all subarrays
def printAllSubArrays(arr):

    seen = set()
    seen.add(0)

    retval = []

    for i in range(len(arr)):

        total = 0

        for j in range(i, len(arr)):
            total += arr[j]

            if total in seen:
                retval.append([i, j])

    return retval


def printSubArray(start, end, arr):

    print('[', end = '')

    for i in range(start, end + 1):
        print(arr[i], end = ' ')

    print(']')

for subarray in printAllSubArrays(tc2):
    printSubArray(subarray[0], subarray[1], tc1)

