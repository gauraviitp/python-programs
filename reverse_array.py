class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.

        Reverse array using reversed function
        """
        nums.reverse()

        nums[0:k] = list(reversed(nums[0:k]))
        nums[k::] = list(reversed(nums[k::]))

        return nums
