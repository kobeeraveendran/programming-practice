# solving problems from https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# for fun

# problem 1
def problem1():
    return [x for x in range(2000, 3201) if (x % 7 == 0 and x % 5 != 0)]

#print(problem1())

def problem2(n):
    if n == 1 or n == 0:
        return 1

    return n * problem2(n - 1)

#print(problem2(8))
