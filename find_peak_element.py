class Solution:
    def findPeakElement(self, a):
        """
        Binary Search
        """

        n = len(a)
        lo = 0
        hi = n - 1

        while lo < hi:

            mid = (lo + hi) // 2

            if a[mid] > a[mid+1]:
                hi = mid
            else:
                lo = mid+1

        return lo
