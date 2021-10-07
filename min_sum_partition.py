import math


class Solution:
    def minDifference(self, arr, n):
        # code here

        bitset = 1

        for val in arr:
            bitset = bitset | bitset << val

        total = sum(arr)

        res = math.inf

        for val in range(0, total//2 + 1):
            if bitset >> (total - val) & 1 == 1:
                res = min(res, abs(total-2*val))

        return res
