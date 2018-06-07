def arrayMaxConsecutiveSum(inputArray, k):
    curr_sum = sum(inputArray[0:k])
    max_sum = curr_sum

    # as we shift over to the next index, subtract the index that is
    # no  longer part of the sum, and add the new index to the current sum
    for i in range(k, len(inputArray) - k + 1):
        curr_sum = curr_sum - inputArray[i] - inputArray[i - k]
        max_sum = max(curr_sum, max_sum)

    return max_sum