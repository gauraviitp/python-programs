from sortedcontainers import SortedList


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        s = SortedList()

        for num in nums:
            i = s.bisect_left(num)

            if i == len(s):
                s.add(num)

            else:
                s.pop(i)
                s.add(num)

        return len(s)
