def areSimilar(a, b):

    if str(a) == str(b):
        return True

    a_diff = []
    b_diff = []

    for i in range(len(a)):
        if a[i] != b[i]:
            a_diff.append(a[i])
            b_diff.append(b[i])
    
    a_diff.reverse()

    return len(a_diff) == 2 and str(a_diff) == str(b_diff)