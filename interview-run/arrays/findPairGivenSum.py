def find_pair_sorted(array, target):
    pair = []

    left = 0
    right = -1

    while(left != right):
        curr_sum = array[left] + array[right]
        
        if curr_sum == target:
            return [array[left], array[right]]

        elif curr_sum < target:
            left += 1

        else:
            right -= 1

    return []

# works on unsorted arrays and also returns all pairs that match the sum, not just the first encountered
def find_pair_complete(array, target):
    pairs = []

    seen = set()

    for num in array:
        if target - num in seen:
            pairs.append([num, target - num])

        else:
            seen.add(num)

    return pairs

arr = [8, 7, 2, 5, 3, 1]

arr_sorted = [1, 2, 3, 5, 7, 8]
target = 10

print(find_pair_sorted(arr_sorted, target))

print(find_pair_complete(arr, target))