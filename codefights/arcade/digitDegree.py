def digitDegree(n):
    num_as_string = str(n)
    num_iters = 0

    while len(num_as_string) > 1:
        n = sum([eval(x) for x in num_as_string])
        num_as_string = str(n)
        num_iters += 1

    return num_iters