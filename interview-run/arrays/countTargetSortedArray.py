def countTargetSortedArray(array, target):

    left = 0
    size = len(array)
    right = size - 1

    while left != size and array[left] != target:
        left += 1

    while right >= 0 and array[right] != target:
        right -= 1

    res = right - left + 1

    return res if res > 0 else 0

tc1 = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]

print(countTargetSortedArray(tc1, 10))
print(countTargetSortedArray(tc1, 5))
print(countTargetSortedArray(tc1, 6))