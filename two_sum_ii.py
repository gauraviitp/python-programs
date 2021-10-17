import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i, num in enumerate(numbers):
            complement = target - num

            pos = bisect.bisect_left(numbers, complement, i+1, n)

            if pos < n and numbers[pos] == complement:
                return [i+1, pos+1]
