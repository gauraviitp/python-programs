# Uses python3

import sys
from functools import lru_cache

# sys.stdin = open('input.txt')


def lcs2(a, b):
    # write your code here

    m = len(a)
    n = len(b)

    @lru_cache(None)
    def lcs(i, j):

        if i == m or j == n:
            return 0

        if a[i] == b[j]:
            return 1 + lcs(i+1, j+1)

        else:
            return max(lcs(i+1, j), lcs(i, j+1))

    return lcs(0, 0)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
