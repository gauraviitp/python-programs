class Solution:
    def maxFruits(self, arr, n, m):

        # sliding window

        s = e = 0
        cursum = maxsum = 0

        while e < n + m:

            cursum += arr[e % n]

            if e-s+1 == m:
                maxsum = max(maxsum, cursum)

                cursum -= arr[s % n]
                s += 1

            e += 1

        return maxsum


sol = Solution()
print(sol.maxFruits([2, 1, 3, 5, 0, 1, 4], 7, 3))
