import functools
import math
import sys

"""
Ctrl+/ Toggle line comment
Shift+Alt+A Toggle block comment
"""

sys.setrecursionlimit(2 * 10**6)


def read_ints():
    return map(int, input().split())


def solve():
    t, = read_ints()

    for test_case in range(1, t+1):

        n, = read_ints()

        arr = list(read_ints())

        result = 0

        print(f'Case #{test_case}: {result}')


if __name__ == '__main__':
    solve()
