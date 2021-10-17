class Solution:
    """
    min with key function

    Squares of a sorted array
    """

    def sortedSquares(self, nums):

        n = len(nums)

        min_pos = min(range(n), key=lambda x: abs(nums[x]))

        left = min_pos
        right = min_pos + 1

        while left >= 0 or right < n:

            if left >= 0 and right < n:
                if abs(nums[left]) <= abs(nums[right]):
                    yield nums[left] ** 2
                    left -= 1
                else:
                    yield nums[right] ** 2
                    right += 1

            elif left >= 0:
                yield nums[left] ** 2
                left -= 1
            else:
                yield nums[right] ** 2
                right += 1
