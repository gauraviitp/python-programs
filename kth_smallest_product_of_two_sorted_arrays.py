import bisect
from typing import List


class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def check(product):

            total = 0

            for val1 in nums1:
                if val1 == 0 and product >= 0:
                    total += len(nums2)
                    continue

                target = product//val1

                # include all the numbers that are equal to or less than target
                total += bisect.bisect_right(nums2, target)

            return total

        lo, hi = -10**10, 10**10

        while lo + 1 < hi:
            mid = (lo + hi)//2

            # lo and hi will be assigned mid

            if check(mid) >= k:
                hi = mid

            else:
                lo = mid

        return hi


sol = Solution()
res = sol.kthSmallestProduct(
    [-4, -2, 0, 3],
    [2, 4],
    6
)

print(res)
