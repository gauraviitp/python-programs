import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i, num in enumerate(numbers):
            complement = target - num

            pos_left = bisect.bisect_left(numbers, complement)
            pos_right = bisect.bisect_right(numbers, complement)

            if pos_left != pos_right:
                if pos_left != i:
                    return [i+1, pos_left+1]
                if pos_right > 0 and pos_right - 1 != i:
                    return [i+1, pos_right]
