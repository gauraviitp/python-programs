from sys import stdout as ostream
from sys import stdin as istream
import heapq
import math

f = istream = open('input.txt')
o = ostream = open('output.txt', 'w')

def read_t():
    return int(f.readline())

"""
    Oversized pancake flipper
    QR - 2017
"""

def solve_oversized_pancake_flipper():
    t = read_t()
    for test_no in range(1, t + 1):
        s, k = f.readline().split()
        s = list(s)
        k = int(k)
        n = len(s)
        count = 0
        for i in range(n - k + 1):
            if s[i] == '-':
                for j in range(i, i + k):
                    if s[j] == '+': s[j] = '-'
                    else: s[j] = '+'
                count += 1
        possible = True
        for char in s:
            if char == '-':
                possible = False
                break
        ans = str(count) if possible else 'IMPOSSIBLE'
        o.write(f"Case #{test_no}: {ans}\n")

"""
    Tidy numbers
    QR - 2017
"""

def solve_tidy_numbers():
    t = read_t()
    for test_no in range(1, t + 1):
        number_list = list(map(int, list(f.readline().strip())))
        n = len(number_list)
        i = 1
        change_required = False
        for i in range(1, n):
            if number_list[i] < number_list[i - 1]:
                change_required = True
                break
        ans = []
        if change_required:
            first = i - 1
            for j in range(i):
                if number_list[j] == number_list[i - 1]:
                    first = j
                    break
            if first - 1 >= 0: ans = number_list[:first]
            ans.append(number_list[first] - 1)
            ans.extend([9] * (n - first - 1))
        else:
            ans = number_list
        ans_no_zeros = []
        check_first_zero = True
        for number in ans:
            if number == 0 and check_first_zero:
                continue
            if number != 0:
                check_first_zero = False
            ans_no_zeros.append(number)
        ans_no_zeros = list(map(str, ans_no_zeros))
        o.write(f"Case #{test_no}: {''.join(ans_no_zeros)}\n")

"""
    Bathroom Stalls - small 2
    QR - 2017
"""

def solve_bathroom_stalls():
    t = read_t()
    for test_no in range(1, t + 1):
        n, k = map(int, f.readline().strip().split())
        heap = [-n]
        heapq.heapify(heap)
        x0, x1 = 0, 0
        for _ in range(k):
            top = -heap[0]
            x0 = math.ceil((top - 1) / 2)
            x1 = math.floor((top - 1) / 2)
            heapq.heappop(heap)
            if x0 > 0: heapq.heappush(heap, -x0)
            if x1 > 0: heapq.heappush(heap, -x1)
        if x0 < x1: x0, x1 = x1, x0
        o.write(f"Case #{test_no}: {x0} {x1}\n")

"""
    Bathroom stalls - Large
    QR - 2017
"""

def solve_bathroom_stalls_large():
    t = read_t()
    for test_no in range(1, t + 1):
        n, k = map(int, f.readline().strip().split())
        heap = [-n]
        dict_ = {n: 1}
        x0, x1 = 0, 0
        p = 0
        while True:
            x = -heap[0]
            x0 = (x - 1) // 2
            x1 = (x // 2)
            c_x  = dict_[x]
            p += c_x
            if p >= k:
                break
            del dict_[x]
            heapq.heappop(heap)
            if x0 > 0: 
                if x0 in dict_:
                    dict_[x0] += c_x
                else:
                    dict_[x0] = c_x
                    heapq.heappush(heap, -x0)
            if x1 > 0: 
                if x1 in dict_:
                    dict_[x1] += c_x
                else:
                    dict_[x1] = c_x
                    heapq.heappush(heap, -x1)
        if x0 < x1: x0, x1 = x1, x0
        o.write(f"Case #{test_no}: {x0} {x1}\n")
    

"""
    Alphabet Cake
    Round 1A - 2017
"""

def solve_alphabet_cake():
    t = read_t()
    for test_no in range(1, t + 1):
        r, c = map(int, f.readline().strip().split())
        grid = [[] for _ in range(r)]
        for i in range(r):
            grid[i] = list(f.readline().strip())
        for i in range(r):
            for j in range(1, c):
                if grid[i][j] == '?' and grid[i][j - 1] != '?':
                    grid[i][j] = grid[i][j - 1]
            for j in range(c - 2, -1, -1):
                if grid[i][j + 1] != '?' and grid[i][j] == '?':
                    grid[i][j] = grid[i][j + 1]

        for i in range(r):
            some_letter = False
            for j in range(c):
                if grid[i][j] !=  '?': some_letter = True
            if not some_letter:
                f_row = -1
                for u_row in range(i - 1, -1, -1):
                    if grid[u_row][0] != '?':
                        f_row = u_row
                        break
                if f_row == -1:
                    for l_row in range(i + 1, r):
                        if grid[l_row][0] != '?':
                            f_row = l_row
                            break
                
                grid[i] = grid[f_row][:]        

        o.write(f"Case #{test_no}:\n")
        for i in range(r):
            for j in range(c):
                o.write(grid[i][j])
            o.write('\n')

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
        o.write(f"Case #{test_no}: {trace} {r} {c}\n")

if __name__ == '__main__':
    solve_latin_square()
    # Flush the output
    o.flush()