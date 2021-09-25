class Solution:
    def subArraySum(self, arr, n, s):

        start = end = 0

        sum_ = 0
        while end < n or start < n:
            if sum_ == s:
                return [start+1, end]

            elif end < n and sum_ < s:
                sum_ += arr[end]
                end += 1

            elif start < n:
                sum_ -= arr[start]
                start += 1

        return [-1]


sol = Solution()
res = sol.subArraySum(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    10,
    15
)

print(res)
