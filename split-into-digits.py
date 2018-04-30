def get_digits(num):
    num_to_list = []

    while num % 10 != 0:
        num_to_list.append(num % 10)
        num = num // 10

    num_to_list.reverse()

    return num_to_list

print("Test 1: " + str(get_digits(789)))