def reverseInteger(a):

    b = 0

    while a > 0:
        b *= 10
        b += a % 10
        a //= 10

    return b

def reverseIntegerWithString(a):

    b = int(str(abs(a))[::-1])

    return b if a >= 0 else -1 * b

print(reverseInteger(93))
print(reverseInteger(-109))

print(reverseIntegerWithString(93))
print(reverseIntegerWithString(-109))