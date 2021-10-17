from bisect import bisect_right


class Solution:
    def search(self, nums, target):
        pos = bisect_right(nums, target)

        if pos == 0 or nums[pos-1] != target:
            return -1
        else:
            return pos-1
