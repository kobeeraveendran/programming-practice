cycles = 8
turn_flag = 0
sequence_list = [1]

print(sequence_list)

for i in range(cycles - 1):
    for j in range(len(sequence_list)):
        if turn_flag == 0:
            sequence_list.insert(j*2, 1)
            turn_flag = 1
        else:
            sequence_list.insert(j*2, 0)
            turn_flag = 0

    sequence_list.append(0)
    turn_flag = 0

    print(sequence_list)
