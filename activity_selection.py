from bisect import bisect_right
from math import inf


class Solution:

    # Function to find the maximum number of activities that can
    # be performed by a single person.
    def activitySelection(self, n, start, end):

        l = list(zip(start, end))

        l.sort(key=lambda x: x[1])

        dp = [(0, 0)]

        for s, e in l:
            # find the index s.t. acitivity ended
            # before start of this activity
            # bisect_right will point you to the index
            # where end time is greater than s-1
            i = bisect_right(dp, (s-1, inf))

            # if this end time has a better answer,
            # add it else it is no  better than previous one
            if dp[i-1][1] + 1 > dp[-1][1]:
                dp += [(e, dp[i-1][1] + 1)]

        return dp[-1][1]


sol = Solution()
print(sol.activitySelection(4, [1, 3, 2, 5], [2, 3, 4, 6]))
