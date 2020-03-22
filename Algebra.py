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



if __name__ == '__main__':
    pass
    