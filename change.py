# Uses python3
import sys


def get_change(m):
    # write your code here

    coins = [10, 5, 1]

    i = 0
    res = 0

    while m:

        q = m//coins[i]
        res += q
        m -= q * coins[i]

        i += 1

    return res


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
