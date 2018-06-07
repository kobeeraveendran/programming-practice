def absoluteValuesSumMinimization(a):
    min_sum = 1000000000000
    ans_list = []

    for num in a:
        temp_sum = sum([abs(a[x] - num) for x in range(len(a))])

        if temp_sum < min_sum:
            min_sum = temp_sum
            ans_list = []
            ans_list.append(num)

        elif temp_sum == min_sum:
            if num not in ans_list:
                ans_list.append(num)

    ans_list.sort()

    return ans_list[0]