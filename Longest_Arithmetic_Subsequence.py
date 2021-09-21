import functools
import math
import sys


sys.setrecursionlimit(2 * 10**6)


def read_ints():
    return map(int, input().split())


def solve_longest_arithmetic():
    t, = read_ints()

    for test_case in range(1, t+1):

        n, = read_ints()

        arr = list(read_ints())

        @functools.lru_cache(None)
        def recurse(pos, diff=math.inf):

            res = 1

            for i in range(pos+1, n):
                if diff == math.inf or diff == arr[i]-arr[pos]:
                    res = max(res, recurse(i, arr[i]-arr[pos]) + 1)

            return res

        res = max([recurse(pos) for pos in range(n)])

        print(f'Case #{test_case}: {res}')


if __name__ == '__main__':
    solve_longest_arithmetic()
