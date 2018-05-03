def mult_table():
    print('\t', end = '')
    for i in range(12):
        print(i + 1, end = '\t')

    print('')

    for i in range(12):
        print(i + 1, end = '\t')
        for k in range(12):
            print((i + 1) * (k + 1), end = '\t')
        print('')

mult_table()