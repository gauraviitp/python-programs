import operator

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """


class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:

        lo = 0
        hi = mountain_arr.length() - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                hi = mid
            else:
                lo = mid + 1

        maxIndex = lo

        def search(lo, hi, op=operator.lt):

            while lo <= hi:
                mid = (lo + hi) // 2

                val = mountain_arr.get(mid)

                if val == target:
                    return mid
                if op(val, target):
                    lo = mid + 1
                else:
                    hi = mid - 1

            return -1

        left = search(0, maxIndex)
        if left != -1:
            return left
        else:
            return search(maxIndex, mountain_arr.length() - 1, operator.gt)
