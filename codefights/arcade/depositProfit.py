def depositProfit(deposit, rate, threshold):
    percent_rate = rate / 100
    years = 0

    while deposit < threshold:
        deposit += percent_rate * deposit
        years += 1

    return years