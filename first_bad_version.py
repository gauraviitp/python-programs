# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    # api method
    def isBadVersion(self, n):
        pass

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        lo, hi = 1, n

        while lo < hi:

            mid = (lo + hi) // 2

            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
