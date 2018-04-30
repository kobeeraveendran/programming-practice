# takes 2 sorted lists and merges them into a new sorted list
def mergesort(list1, list2):
    curr1 = 0
    curr2 = 0

    new_sorted = []

    while curr1 != len(list1) and curr2 != len(list2):
        if list1[curr1] < list2[curr2]:
            new_sorted.append(list1[curr1])
            curr1 += 1

        elif list2[curr2] < list1[curr1]:
            new_sorted.append(list2[curr2])
            curr2 += 1

        else:
            new_sorted.append(list1[curr1])
            curr1 += 1
            curr2 += 1

    new_sorted.append(max(max(list1), max(list2)))

    return new_sorted

test1_list1 = [1, 4, 6]
test1_list2 = [2, 3, 5]

print("Merged and sorted test 1: " + str(mergesort(test1_list1, test1_list2)))

test2_list1 = [1, 1, 5, 6]
test2_list2 = [2, 3, 5, 7]

print("Merged and sorted test 2: " + str(mergesort(test2_list1, test2_list2)))