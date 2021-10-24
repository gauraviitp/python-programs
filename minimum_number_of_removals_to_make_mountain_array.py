import bisect
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def lis(arr):

            s = []

            for num in arr:
                i = bisect.bisect_left(s, num)
                if i == len(s):
                    s.append(num)
                else:
                    s[i] = num

            return len(s)

        ret = 0

        for i in range(1, n-1):

            pre = [num for num in nums[:i] if num < nums[i]] + [nums[i]]

            post = [nums[i]] + [num for num in nums[i+1:] if num < nums[i]]

            lisPre = lis(pre)
            lisPost = lis(post[::-1])

            if lisPre >= 2 and lisPost >= 2:
                ret = max(ret, lisPre + lisPost - 1)

        return n - ret
