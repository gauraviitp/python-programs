import functools
import math
import sys


sys.setrecursionlimit(2 * 10**6)


def read_ints():
    return map(int, input().split())


def solve():
    t, = read_ints()

    for test_case in range(1, t+1):

        n, a, b, c = read_ints()

        result = None

        lst = [0] * (n)

        def generate_all(i):

            nonlocal result

            if i == n:

                max_left = -math.inf
                count_a = 0
                for pos in range(n):
                    if max_left <= lst[pos]:
                        count_a += 1
                        max_left = max(max_left, lst[pos])

                max_right = -math.inf
                count_b = 0
                for pos in range(n-1, -1, -1):
                    if lst[pos] >= max_right:
                        count_b += 1
                        max_right = max(max_right, lst[pos])

                max_all = max(lst)

                count_c = lst.count(max_all)

                if a == count_a and b == count_b and c == count_c:
                    result = lst[:]

                return

            for val in range(1, n+1):
                lst[i] = val
                generate_all(i+1)

        generate_all(0)

        print(
            f'Case #{test_case}: {" ".join(map(str, result)) if result else "IMPOSSIBLE"}')


if __name__ == '__main__':
    solve()
