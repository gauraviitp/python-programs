class Solution:
    def canReach(self, A, N):
        j = 0

        for i in range(N):

            if j < i:
                return False

            j = max(i+A[i], j)

        return True


sol = Solution()

print(sol.canReach([1, 0, 2], 3))
