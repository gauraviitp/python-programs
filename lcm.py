# Uses python3
def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


def lcm(a, b):
    return a * b//gcd(a, b)


a, b = map(int, input().strip().split())

print(lcm(a, b))
