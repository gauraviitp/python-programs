import sys
from functools import lru_cache

sys.setrecursionlimit(10**6)

sys.stdin = open(f'Kickstart\\input.txt')
sys.stdout = open(f'Kickstart\\output.txt', 'w')


# F(plate_number, stack_number):
# Choose x plates from the stack#stack_number
# for x in [0..plate_number]:
#       res = max(res, pre_sum[x] + F(plate_number-x, stack_number))

def read_ints():
    return map(int, input().split())


def solve_plates():

    t, = read_ints()

    for test_case in range(1, t+1):

        n, k, p = read_ints()

        stacks = []

        for _ in range(n):
            stacks.append(list(read_ints()))

        preSum = [[0 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, k+1):
                preSum[i][j] = preSum[i][j-1] + stacks[i-1][j-1]

        @lru_cache(None)
        def recurse(plate_number, stack_number):
            if plate_number <= 0 or stack_number <= 0:
                return 0

            res = 0

            for x in range(0, min(plate_number + 1, k + 1)):
                res = max(res, preSum[stack_number][x] +
                          recurse(plate_number - x, stack_number - 1))

            return res

        test_case_result = recurse(p, n)

        print(f'Case #{test_case}: {test_case_result}')


if __name__ == '__main__':
    solve_plates()
