# python3
import sys

#sys.stdin = open('input.txt')


def compute_min_refills(distance, tank, stops):
    # write your code here

    stops = [0] + stops + [distance]

    n = len(stops)

    res = 0

    curPos = 0

    while curPos < n:

        nextPos = pos = curPos

        while pos < n and stops[pos] - stops[curPos] <= tank:
            nextPos = pos
            pos += 1

        if pos == n:
            return res

        if nextPos == curPos:
            return -1

        res += 1

        curPos = nextPos

    return res


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
