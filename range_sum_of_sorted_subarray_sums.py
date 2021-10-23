import heapq
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        MOD = 10**9 + 7

        for i, num in enumerate(nums):
            heapq.heappush(heap, (num, i+1))

        res = 0

        for i in range(1, right+1):
            num, j = heapq.heappop(heap)

            if i >= left:
                res = (res + num) % MOD

            if j < n:
                heapq.heappush(heap, (num+nums[j], j+1))

        return res
