def knapsackLight(value1, weight1, value2, weight2, maxW):
    knapsack = {value1: weight1, value2: weight2}

    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 > maxW and weight2 > maxW:
        return 0
    else:
        return max(value1, value2) if knapsack[max(value1, value2)] <= maxW else min(value1, value2)