import functools
import math
import sys

sys.setrecursionlimit(2 * 10**6)

sys.stdin = open(f'Kickstart\\2020_D_Alien_Piano_input.txt')
sys.stdout = open(f'Kickstart\\2020_D_Alien_Piano_output.txt', 'w')

"""
Let F(i, j) be minimum number of rule violations required to convert first
i notes such that ith note A[i] is converted to note j of the alien piano.
Then, the answer is the minimum F(K, j) over all j, 1 <= j <= 4.

F(1, j) = 0 for all j.
For i > 1, F(i, j) =  min { F(i-1, j') + P(i, j', j) }

If A[i-1] > A[i]:
    If j' > j, P(i, j', j) = 0 
    Else, P(i, j', j) = 1

"""


def read_ints():
    return map(int, input().split())


def solve_alien_piano():

    t, = read_ints()

    for test_case in range(1, t + 1):

        k, = read_ints()
        notes = list(read_ints())

        @functools.lru_cache(None)
        def recurse(i, j):
            """
            recurse(i, j) returns the minimum number of violations to convert first i
            notes such that ith note notes[i] is converted to note j of the alien piano.
            """

            if i == 0:
                return 0

            return_val = math.inf

            for j_p in range(1, 5):

                penalty = 0

                # If previous note was higher in local piano
                # but current note is lower or equal in alien piano
                # then penalty.
                if notes[i-1] > notes[i] and j_p <= j:
                    penalty = 1

                if notes[i-1] < notes[i] and j_p >= j:
                    penalty = 1

                if notes[i-1] == notes[i] and j_p != j:
                    penalty = 1

                return_val = min(recurse(i-1, j_p) + penalty, return_val)

            return return_val

        print(f'Case #{test_case}: {min(recurse(k-1, j) for j in range(1, 5))}')


if __name__ == '__main__':
    solve_alien_piano()
