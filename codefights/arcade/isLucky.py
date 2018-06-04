# Kobee Raveendran
# isLucky - CodeFights

# given a ticket number n with an even number of digits, 
# determine whether hte ticket number is 'lucky' or not;
# that is, whether the sum of the first half of the digits
# is equal to the sum of the second half of digits

def isLucky(n):
    # convert integer n into a list of its digits
    n = [int(x) for x in str(n)]

    sum1 = 0
    sum2 = 0

    # determine sums
    for i in range(len(n) // 2):
        sum1 += n[i]
        sum2 += n[(len(n) // 2) + i]

    return sum1 == sum2

print(isLucky(10))