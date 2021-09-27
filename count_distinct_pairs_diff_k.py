# User function Template for python3


class Solution:
    def TotalPairs(self, nums, k):
        s = set(nums)
        res = 0
        for num in list(s):
            if k == 0 and num in s:
                res += 1
            else:
                if num + k in s:
                    res += 1
                if num - k in s:
                    res += 1
            if num in s:
                s.remove(num)
        return res


sol = Solution()
print(sol.TotalPairs([11, 6, 10, 5, 11, 16], 5))
