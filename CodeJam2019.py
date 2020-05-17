from sys import stdout as ostream
from sys import stdin as istream
import heapq
import math

f = istream = open('input.txt')
o = ostream = open('output.txt', 'w')

"""
    QR - 2019
"""

def solve_latin_square():
    t = int(f.readline())
    for test_no in range(1, t + 1):
        n = int(f.readline())
        m = []
        for _ in range(n):
            m.append(list(map(int, f.readline().split())))
        # trace
        trace = 0
        for i in range(n):
            trace += m[i][i]
        # duplicate rows
        r = 0
        for i in range(n):
            okay = True
            seen = [False] * (n + 1)
            for j in range(n):
                if seen[m[i][j]]:
                    okay = False
                    break
                seen[m[i][j]] = True
            if not okay:
                r += 1
        # duplicate columns
        c = 0
        for j in range(n):
            okay = True
            seen = [False] * (n + 1)
            for i in range(n):
                if seen[m[i][j]]:
                    okay = False
                    break
                seen[m[i][j]] = True
            if not okay:
                c += 1
        o.write("Case #%d: %d %d %d\n" % (test_no, trace, r , c))

def solve_min_paranthesis():
    t = int(f.readline())
    for test_no in range(1, t + 1):
        s = f.readline().strip()
        res = []
        prev = -1
        for cstr in s:
            c = int(cstr)
            if prev == -1:
                res.extend(['('] * c)
            elif c > prev:
                res.extend(['('] * (c - prev))
            elif c < prev:
                res.extend([')'] * (prev - c))
            res.append(cstr)
            prev = c  
        res.extend([')'] * int(s[len(s) - 1]))
        o.write("Case #%d: %s\n" % (test_no, ''.join(res)))

def solve_overlapping_schedules():
    t = int(f.readline())
    for test_no in range(1, t + 1):
        n = int(f.readline())
        a = []
        for i in range(n):
            l = list(map(int, f.readline().strip().split()))
            l.append(i)
            a.append(l)
        a.sort()
        c_next, j_next = a[0][0], a[1][0]
        okay = True
        res = [''] * n
        for s, e, i in a:
            if s >= c_next:
                res[i] = 'C'
                c_next = max(c_next, e)
            elif s >= j_next:
                res[i] = 'J'
                j_next = max(j_next, e)
            else:
                okay = False
                break
        o.write("Case #%d: %s\n" % (test_no, ''.join(res) if okay else 'IMPOSSIBLE'))



if __name__ == '__main__':
    solve_overlapping_schedules()
    # Flush the output
    o.flush()