# Uses python3
import sys
import math

#sys.stdin = open('input.txt')

coins = [1, 3, 4]


def get_change(m):
    # write your code here

    dp = [math.inf] * (m+1)
    dp[0] = 0

    for amount in range(1, m+1):

        for coin in coins:

            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
