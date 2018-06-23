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

def problem3(n):
    retval = {}
    for i in range(1, n + 1):
        retval[i] = i ** 2

    return retval

#print(problem3(8))

def problem4(input):
    nums = input.split(',')
    as_tuple = tuple(nums)

    print(nums)
    print(as_tuple)

#problem4('34,67,55,33,12,98')

class problem5(object):
    def __init__(self):
        self.input_str = ''

    def getString(self):
        self.input_str = input()
    
    def printString(self):
        print(self.input_str)

str_obj = problem5()
#str_obj.getString()
#str_obj.printString()
import numpy as np
import math

def problem6(input_sequence):
    vals = input_sequence.split(',')
    c = 50
    h = 30
    retval = ''

    for i in range(len(vals)):
        q = int(np.round(math.sqrt((2 * c * int(vals[i])) / h)))
        if i == len(vals):
            retval += str(q)
        else:
            retval += str(q) + ','

    return retval

#print(problem6('100,150,180'))