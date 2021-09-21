# Uses python3
import sys
from functools import lru_cache

# sys.stdin = open('input.txt')


def optimal_weight(W, w):
    # write your code here

    n = len(w)

    @lru_cache(None)
    def knapsack(remWeight, i):

        if i == n:
            return 0

        res = 0

        if w[i] <= remWeight:
            # include weight
            res = max(res, knapsack(remWeight - w[i], i+1) + w[i])

        res = max(res, knapsack(remWeight, i+1))  # exclude weight

        return res

    return knapsack(W, 0)


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
