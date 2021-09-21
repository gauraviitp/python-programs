# Uses python3
import sys
import random

#sys.stdin = open('input.txt')


def partition3(a, l, r):
    # write your code here

    x = a[r]  # partition element

    lo = cur = l
    hi = r - 1

    # when the loop terminates
    # cur == hi + 1 and a[cur] > x
    while cur <= hi:

        if a[cur] < x:
            a[lo], a[cur] = a[cur], a[lo]
            lo += 1
            cur = max(lo, cur)

        elif a[cur] > x:
            a[cur], a[hi] = a[hi], a[cur]
            hi -= 1

        else:
            cur += 1

    a[cur], a[r] = a[r], a[cur]

    return lo, hi


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    lo, hi = partition3(a, l, r)
    randomized_quick_sort(a, l, lo - 1)
    randomized_quick_sort(a, hi + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
