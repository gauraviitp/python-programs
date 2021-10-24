from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        s = []  # a sorted list

        for num in nums:
            i = bisect_left(s, num)

            if i == len(s):
                s.append(num)

            else:
                s[i] = num

        return len(s)
