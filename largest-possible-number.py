def formLargestNumber(input):
    answer = ""
    # find max value based on 1st digit
    for i in range(len(input)):
        max, index = findMax(input)
        answer += str(max)
        del input[index]

    return answer
    
        
def findMax(input):
    max = 0
    index = 0

    for i in range(len(input)):
        if int(str(input[i])[0]) > max:
            max = int(str(input[i])[0])
            index = i

    return input[index], index

posList = [50, 2, 1, 9]
print("Largest possible number: " + str(formLargestNumber(posList)))