from functools import lru_cache


class Solution:
    def canCross(self, stones) -> bool:

        if stones[1] != 1:
            return False

        S = set(stones)

        @lru_cache(None)
        def recurse(pos, step):

            if pos == stones[-1]:
                return True

            for nextStep in [step-1, step, step+1]:

                if nextStep > 0 and (pos + nextStep) in S:
                    res = recurse(pos + nextStep, nextStep)

                    if res:
                        return True

        return recurse(1, 1)


sol = Solution()
sol.canCross([0, 1, 2, 5, 6, 9, 10, 12, 13, 14,
              17, 19, 20, 21, 26, 27, 28, 29, 30])
