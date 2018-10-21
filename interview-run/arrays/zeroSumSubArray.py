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

print("Zero sum subarray exists") if zeroSumSubArray(tc1) else print("Zero sum subarray does not exist")
