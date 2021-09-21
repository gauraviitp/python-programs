# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    a0, a1 = 0, 1
    for _ in range(n-1):
        x = (a0 + a1) % 10

        a0 = a1
        a1 = x

    return a1


n = int(input())
print(calc_fib(n))
