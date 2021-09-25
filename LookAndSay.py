# User function Template for python3

class Solution:

    def lookandsay(self, n):

        def recurse(i):
            if i == 1:
                return [1]

            pre = recurse(i-1)
            count = 1
            preVal = pre[0]

            res = []

            for i in range(1, len(pre)):
                if pre[i] == preVal:
                    count += 1
                    continue
                else:
                    res += [count] + [preVal]
                    preVal = pre[i]
                    count = 1

            res += [count] + [preVal]

            return res

        return ''.join(map(str, recurse(n)))


sol = Solution()
print(sol.lookandsay(5))
