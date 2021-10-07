
class Solution:
    def isKPartitionPossible(self, a, k):
        # code here

        a.sort()
        n = len(a)

        def recurse(i, pSums):
            if i == n:
                if all(pSum and pSum == subset_sum for pSum in pSums):
                    return True

                return False

            res = False
            for j in range(k):
                if pSums[j] + a[i] > subset_sum:
                    continue

                pSums[j] += a[i]
                res = recurse(i+1, pSums)
                pSums[j] -= a[i]

                if res:
                    return True

            return res

        total = sum(a)
        subset_sum = total // k
        if total % k == 0:
            return recurse(0, [0 for _ in range(k)])
        return False


sol = Solution()
print(sol.isKPartitionPossible([2, 1, 4, 5, 6], 3))
