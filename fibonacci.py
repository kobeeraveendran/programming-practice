def fibonacci(n = 101):
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)

    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list

print(fibonacci(101))