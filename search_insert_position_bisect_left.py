class Solution:

    def searchInsert(self, nums, target: int) -> int:
        """
        Implements bisect_left
        """

        lo, hi = 0, len(nums) - 1

        while lo <= hi:

            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                lo = mid + 1  # lo points to index for which element is greater than equal to target

            else:
                hi = mid - 1

        return lo  # when loop exits lo must be pointing to element that is just greater than target
