# Uses python3

# matrix multiply and b modulo m


def matrix_multiply(a, b, m):
    res = []

    for i in range(2):
        res.append([])

        for j in range(2):
            val = 0

            for k in range(2):
                val += a[i][k] * b[k][j]
                val = val % m

            res[i].append(val)

    return res

# raises matrix a to the power b


def power(a, b, m):

    res = [[1, 0],
           [0, 1]]

    while b:
        if b & 1:
            res = matrix_multiply(res, a, m)

        a = matrix_multiply(a, a, m)
        b = b >> 1

    return res

# nth fib number mod m


def fib(n, m):
    if n <= 1:
        return n

    mat = [[1, 1], [1, 0]]

    res = power(mat, n-1, m)

    return res[0][0]


def sum(n, m):
    return (fib(n+2, m) - 1) % m


a = int(input())
print(sum(a, 10))
