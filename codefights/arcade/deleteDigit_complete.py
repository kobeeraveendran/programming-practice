def deleteDigit(n):
    max_num = 0
    digits = list(str(n))

    for i in range(len(digits)):
        temp_list = digits[:i] + digits[i + 1:]
        temp_num = int(''.join(temp_list))
        if temp_num > max_num:
            max_num = temp_num
        
    return max_num