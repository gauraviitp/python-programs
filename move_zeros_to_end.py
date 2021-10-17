class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Two pointer solution.
        """

        n = len(nums)

        insert_pos = cur_pos = 0

        while cur_pos < n:

            if nums[cur_pos] == 0:
                cur_pos += 1

            else:
                nums[insert_pos] = nums[cur_pos]
                insert_pos += 1
                cur_pos += 1

        while insert_pos < n:
            nums[insert_pos] = 0
            insert_pos += 1
