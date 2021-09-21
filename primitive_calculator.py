# Uses python3
import sys
import math

# sys.stdin = open('input.txt')


def optimal_sequence(n):

    # dp[n] is min steps to get to n
    dp = [math.inf] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):

        # i = j + 1
        dp[i] = min(dp[i], dp[i-1] + 1)

        # i = j * 2
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        # i = j * 3
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    res = []

    cur = n

    while cur >= 1:

        res.append(cur)

        next = cur-1
        minVal = dp[cur-1]

        if cur % 2 == 0 and dp[cur//2] < minVal:
            minVal = dp[cur//2]
            next = cur//2

        if cur % 3 == 0 and dp[cur//3] < minVal:
            next = cur//3

        # loop variant
        cur = next

    return list(reversed(res))


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
