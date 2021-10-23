import math
from sortedcontainers import SortedSet
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        rows = len(matrix)
        cols = len(matrix[0])

        res = -math.inf

        for left in range(cols):

            sums = [0] * rows

            for right in range(left, cols):

                for row in range(rows):
                    sums[row] += matrix[row][right]

                pre = 0
                presums = SortedSet([0])

                for s in sums:
                    pre += s

                    j = presums.bisect_left(pre-k)

                    if j < len(presums):
                        res = max(res, pre-presums[j])

                    presums.add(pre)

        return res


sol = Solution()
res = sol.maxSumSubmatrix(
    [[1, 0, 1], [0, -2, 3]],
    2
)

print(res)
