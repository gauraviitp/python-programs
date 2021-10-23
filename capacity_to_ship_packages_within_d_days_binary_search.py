from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(w):
            d = 1

            group = 0
            for x in weights:
                group += x

                if group > w:
                    group = x
                    d += 1

            return d <= days

        lo, hi = 0, sum(weights)

        while lo < hi:

            mid = (lo + hi) // 2

            if check(mid):
                hi = mid

            else:
                lo = mid + 1

        return lo


sol = Solution()
print(sol.shipWithinDays([1, 2, 3, 1, 1], 4))
