import sys
import collections
import math
import itertools

from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(2 * 10**6)

#sys.stdin = open(f'input.txt')
#sys.stdout = open(f'output.txt', 'w')


def read():
    return list(map(int, input().split()))


def solve():
    t, n, _ = read()

    for _ in range(1, t+1):

        arr = [1, 2]

        d = {}

        for i in range(3, (n+1)):

            done = False
            lo, hi = 0, i-2

            while lo < hi:

                j = (lo + hi) // 2
                k = j + 1

                t = [i, arr[j], arr[k]]
                t.sort()
                t = tuple(t)

                median = -1

                if t in d:
                    median = d[t]

                else:
                    print(f'{i} {arr[j]} {arr[k]}')

                    median, = read()

                    d[t] = median

                if median == arr[j]:
                    hi = j

                elif median == i:
                    arr.insert(k, i)
                    done = True
                    break

                else:
                    lo = j + 1

            if not done:
                if lo == i-2:
                    arr.append(i)
                else:
                    arr.insert(lo, i)

        print(" ".join(map(str, arr)))

        res, = read()
        if res == -1:
            break


solve()
