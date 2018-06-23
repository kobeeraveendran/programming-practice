import string

lookup_table = list(string.digits + string.ascii_lowercase)

def mirrorBase(num, base1, base2):
    # convert to base 10, then base2
    num = base_convert(int(num, base1), base2)

    return num == num[::-1]

def base_convert(num, target_base):
    remainders = []

    while num > 0:
        remainders.append(lookup_table[num % target_base])
        num //= target_base

    return ''.join(reversed(remainders))
print(mirrorBase('121', 4, 2))
print(mirrorBase('505', 6, 7))