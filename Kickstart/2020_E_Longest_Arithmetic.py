import functools
import math
import sys


sys.setrecursionlimit(2 * 10**6)


def read_ints():
    return map(int, input().split())


def solve():
    t, = read_ints()

    for test_case in range(1, t+1):

        n, = read_ints()

        arr = list(read_ints())

        diff = arr[1] - arr[0]
        result = count = 2

        for end in range(2, n):

            if arr[end] - arr[end-1] == diff:
                count += 1
                result = max(result, count)

            else:
                count = 2
                diff = arr[end] - arr[end-1]

        print(f'Case #{test_case}: {result}')


if __name__ == '__main__':
    solve()
