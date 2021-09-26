from math import inf


def maxSumWithK(a, n, k):

    s = e = 0

    maxsums = [-inf] * n
    cur = 0
    for i in range(n):
        cur = max(cur + a[i], a[i])
        maxsums[i] = cur

    maxsum = -inf
    cursum = 0

    while e < n:
        cursum += a[e]

        if e - s + 1 == k:
            maxsum = max(maxsum, cursum +
                         (maxsums[s-1] if s > 0 else 0), cursum)

            cursum -= a[s]
            s += 1

        e += 1

    return maxsum


print(maxSumWithK([1, 1, 1, 1, 1, 1], 6, 2))
