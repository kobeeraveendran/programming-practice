import time

# version 1 (brute force)
# time complexity: O(n)
def sum1(n):
    sum = 0

    for i in range(n + 1):
        sum += i

    return sum

# version 2 (summation notation)
# time complexity: O(1)
def sum2(n):
    sum = (n * (n + 1)) / 2

    return int(sum)

start1 = time.time()
print("Result of sum1: " + str(sum1(300000000)))
end1 = time.time()
print("Execution time of sum1: " + str(end1 - start1) + "s")
# Note the execution time here: ~14.45 seconds...

start2 = time.time()
print("Result of sum2: " + str(sum2(300000000)))
end2 = time.time()
print("Execution time of sum2: " + str(end2 - start2) + "s")
# but here, the execution time is still ~0 seconds (just an arithmetic operation)