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

def problem7(x, y):
    return [[i * j for i in range(y)] for j in range(x)]

#print(problem7(3, 5))

def problem8(sequence):
    words = sequence.split(',')
    return ','.join(sorted(words))

#print(problem8('without,hello,bag,world'))

def problem9(sequence):
    for i in range(len(sequence)):
        print(sequence[i].upper())

#problem9(['Hello world','Practice makes perfect'])

def problem10(sequence):
    return ' '.join(sorted(list(set(sequence.split(' ')))))

#print(problem10('hello world and practice makes perfect and hello world again'))

def problem11(sequence):
    # convert to base 10
    nums = sequence.split(',')
    return ','.join([x for x in nums if int(x, 2) % 5 == 0])

#print(problem11('0100,0011,1010,1001'))

def problem12():
    return ','.join([str(x) for x in range(1000, 3001) if even_digits(x)])

def even_digits(x):
    even_test = [int(i) % 2 == 0 for i in str(x)]
    return all(even_test)

#print(problem12())

def problem13(sentence):
    letters = 0
    digits = 0

    for char in sentence:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1

    print('LETTERS ' + str(letters))
    print('DIGITS ' + str(digits))

#problem13('hello world! 123')

def problem14(sentence):
    upper_count = sum(1 for char in sentence if char.isupper())
    lower_count = sum(1 for char in sentence if char.islower())

    print(upper_count)
    print(lower_count)

#problem14('Hello world!')

def problem15(digit):
    vals = [str(digit) * i for i in range(1,5)]
    return sum([int(x) for x in vals])

#print(problem15(9))

def problem16(inputlist):
    as_list = inputlist.split(',')
    return ','.join([str(int(x) ** 2) for x in as_list if int(x) % 2 == 1])

#print(problem16('1,2,3,4,5,6,7,8,9'))

def problem17(transactions):
    transactions = [(transaction.split(' ')[0], int(transaction.split(' ')[1])) for transaction in transactions]
    balance = 0
    for transaction in transactions:
        balance += transaction[1] if transaction[0] == 'D' else (-1 * transaction[1])

    return balance

#print(problem17(['D 300', 'D 300', 'W 200', 'D 100']))

import re
def problem18(passwords):
    passwords = passwords.split(',')
    valid_passwords = []

    for password in passwords:
        if len(password) >= 6 and len(password) <= 12 and re.search('[a-z]', password) and re.search('[0-9]', password) and re.search('[A-Z]', password) and re.search('[$#@]', password):
            valid_passwords.append(password)

    print(','.join(valid_passwords))

#problem18('ABd1234@1,a F1#,2w3E*,2We3345')

import operator

def problem19(people):
    as_tuple = [tuple(person.split(',')) for person in people]
    return sorted(as_tuple, key = operator.itemgetter(0, 1, 2))

#print(problem19(['Tom,19,80', 'John,20,90', 'Jony,17,91', 'Jony,17,93', 'Json,21,85']))

def problem20(n):
    for i in range(n):
        if i % 7 == 0:
            yield i

generator = problem20(100)
#for i in generator:
#    print(i)

def problem21(movements):
    movements = [tuple(move.split(' ')) for move in movements]
    delta_y = sum([int(y[1]) for y in movements if y[0] == 'UP']) - sum([int(y[1]) for y in movements if y[0] == 'DOWN'])
    delta_x = sum([int(x[1]) for x in movements if x[0] == 'RIGHT']) - sum([int(x[1]) for x in movements if x[0] == 'LEFT'])

    return round(math.sqrt(delta_x ** 2 + delta_y ** 2))

#print(problem21(['UP 5', 'DOWN 3', 'LEFT 3', 'RIGHT 2']))

def problem22(sentence):
    sentence = sentence.split()
    frequency = {}

    for word in sentence:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_keys = sorted(frequency.keys())

    for key in sorted_keys:
        print(str(key) + ': ' + str(frequency[key]))

#problem22('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')

def problem23(n):
    return n ** 2

#print(problem23(4))

def problem24(function):
    print('Function: ' + function + '()')
    print(eval(function + '.__doc__'))
    print('\n')

#problem24('abs')
#problem24('int')
#problem24('input')

# problem 25
class Person():
    name = 'Person'

    def __init__(self, name = None):
        self.name = name

#kobee = Person()
#kobee.name = 'Kobee'
#print(kobee.name)

def problem26(num1, num2):
    return num1 + num2

#print(problem26(3, 5))