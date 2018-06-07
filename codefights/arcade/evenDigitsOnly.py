def evenDigitsOnly(n):
    string_rep = str(n)

    for i in range(len(string_rep)):
        if eval(string_rep[i]) % 2 != 0:
            return False

    return True