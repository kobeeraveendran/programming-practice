def extractEachKth(inputArray, k):
    removed_list = []
    
    for i in range(len(inputArray)):
        if (i + 1) % k != 0:
            removed_list.append(inputArray[i])

    return removed_list