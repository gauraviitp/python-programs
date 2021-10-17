class Solution:
    def rotate(self, nums, k: int):
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(i, j):
            """
            Reverse elements from index i to j
            """

            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        n = len(nums)

        k %= n

        reverse(0, n - 1)  # reverse all elements

        reverse(0, k - 1)  # reverse first k elements
        reverse(k, n - 1)  # reverse elements from k+1 to end
