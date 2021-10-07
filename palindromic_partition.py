import functools
import math
from sys import setrecursionlimit

setrecursionlimit(10**6)


class Solution:
    """
    Palindromic partitioning function that makes use of Rabin karp idea.
    Run time complexity: O(n*n)
    Space complexity: O(n)
    where n is the length of the string.
    """

    def palindromicPartition(self, string):
        p = 257
        mod = 10**9 + 7

        n = len(string)

        @functools.lru_cache(None)
        def recurse(i):
            if i == n:
                return 0

            hash = ord(string[i])
            hashReverse = ord(string[i])
            pPow = p

            res = math.inf
            for j in range(i+1, n):
                if hash == hashReverse:
                    res = min(res, recurse(j) + 1)

                hash = (hash * p + ord(string[j])) % mod
                hashReverse = (hashReverse + ord(string[j]) * pPow) % mod
                pPow = (pPow * p) % mod

            if hash == hashReverse:
                res = min(res, recurse(n))  # you didn't partition really

            return res

        return recurse(0)


sol = Solution()
print(sol.palindromicPartition('aaabba'))
