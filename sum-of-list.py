def sumOfListFor(input):
    sum = 0
    for i in range(0, len(input)):
        sum += input[i]

    return sum

def sumOfListWhile(input):
    sum = 0
    i = 0
    while (i < len(input)):
        sum += input[i]
        i = i + 1

    return sum

def sumOfListRecursive(inputlist, index, sum = 0):
    if index == 0:
        sum += inputlist[0]
        return sum
    
    else:
        sum += inputlist[index]
        return sumOfListRecursive(input, index - 1, sum)

listylist = [3, 2, 6, 8, 10]
# sum should be 29

print("For loop: " + str(sumOfListFor(listylist)))
print("While loop: " + str(sumOfListWhile(listylist)))
print("Recursion: " + str(sumOfListRecursive(listylist, len(listylist) - 1)))