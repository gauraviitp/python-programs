from math import pi, sin, cos


def fft(a, invert):
    n = len(a)
    if n == 1:
        return

    a0 = [a[2*i] for i in range(n//2)]
    a1 = [a[2*i+1] for i in range(n//2)]

    fft(a0, invert)
    fft(a1, invert)

    ang = 2 * pi / n * (-1 if invert else 1)
    w, wn = complex(1), complex(sin(ang), cos(ang))
    for k in range(n//2):
        a[k] = a0[k] + w * a1[k]
        a[k+n//2] = a0[k] - w * a1[k]

        if invert:
            a[k] /= 2
            a[k + n//2] /= 2

        w *= wn


def multiply(a, b):
    n = 1
    while n < len(a) + len(b):
        n = n << 1

    a += [0] * (n - len(a))
    b += [0] * (n - len(b))

    fft(a, False)
    fft(b, False)

    for i in range(n):
        b[i] *= a[i]

    fft(b, True)

    result = [0] * n
    for i in range(n):
        result[i] = b[i].real

    return result


a = [1, 2]
b = [1, 2]
res = multiply(a, b)
print(res)
