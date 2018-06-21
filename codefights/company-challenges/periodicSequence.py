def periodicSequence(s0, a, b, m):
    sequence = [s0]
    seen = []
    seen_flag = False
    i = 1

    while not seen_flag:
        temp = (a * sequence[i -1] + b) % m

        if temp in seen:
            seen_flag = True
            prev_val = sequence.index(temp)
            return i - prev_val
        else:
            sequence.append(temp)
            seen.append(temp)

        i += 1

    return i


print(periodicSequence(11, 2, 6, 12))