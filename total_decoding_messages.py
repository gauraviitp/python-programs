from functools import lru_cache


class Solution:
    def CountWays(self, str):
        n = len(str)
        mod = 10**9 + 7

        @lru_cache(None)
        def recurse(i):
            if i == n:
                return 1

            res = 0

            if 1 <= int(str[i]) <= 9:
                res = recurse(i+1)

            if i + 1 < n and str[i] != '0' and 1 <= int(str[i:i+2]) <= 26:
                res += recurse(i+2)

            return res % mod

        return recurse(0)


sol = Solution()
print(sol.CountWays("27"))
