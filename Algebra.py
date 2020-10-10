from sys import stdin as istream
from sys import stdout as ostream

def binary_exponentiation(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a
        b >>= 1
        a *= a
    return res

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a% b)

"""
    extended euclidean algorithm
    finds gcd along with x and y for the equation a.x + b.y = gcd(a, b)
    compares a.x + b.y = g to (b  mod a).x1 + a.y = g where b mod a = b - (b // a) * a
"""
def gcd_extended(a, b, x: list, y: list):
    if a == 0:
        x[0] = 0
        y[0] = 1
        return b
    x1, y1 = [0], [0]
    d = gcd_extended(b % a, a, x1, y1)
    x[0] = y1[0] - (b // a) * x1[0]
    y[0] = x1[0]
    return d

"""
    linear diophantine equation - any solution
    finds solution to equation a.x + b.y = c
    first finds solution to a.xg + b.yg = g then multiplies the equation by c // g
"""

def linear_diophantine_equation_any_solution(a, b, c, x: list, y: list, g: list):
    g[0] = gcd_extended(a, b, x, y)
    if c % g[0] != 0:
        return False
    x[0] = x[0] * c // g[0]
    y[0] = y[0] * c // g[0]
    if a < 0:   x[0] = -x[0]
    if b < 0:   y[0] = -y[0]
    return True

"""
    F(n + 2) = F(n + 1) + F(n)
    F(n + 3) = F(n + 2) + F(n + 1) = 2F(n + 1) + F(n)
    F(n + 4) = F(n + 3) + F(n + 2) = 2F(n + 2) + F(n + 1) = 3F(n + 1) + 2F(n)
    F(n + k) = F(k)F(n + 1) + F(k - 1)F(n)
    F(2n) = F(n)F(n + 1) + F(n - 1)F(n) = F(n)[F(n + 1) + F(n - 1)] = F(n)[2F(n + 1) - F(n)]
    F(2n + 1) = sq[F(n+1)] + sq(F(n))
"""

def nth_fibonacci(n):
    if n == 0:
        return [0, 1]
    nby2 = nth_fibonacci(n >> 1)
    fn, fn_1 = nby2[0], nby2[1]
    c = fn * (2 * fn_1 - fn)
    d = fn_1 * fn_1 + fn * fn
    if n & 1:
        return [d, c + d] # if n == 3, then f(2k) = f(2), therefore return [f(2k + 1), f(2k + 2)]
    else:
        return [c, d]


def factorization_trial_division(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n%d == 0:
            n//=d
            if d in factors: factors[d] += 1
            else: factors[d]=1
        d+=1
    if n>1: factors[n]=1
    return factors

if __name__ == '__main__':
    pass