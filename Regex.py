import re


class Solution:
    def solveEquation(self, equation: str) -> str:

        sign = 1

        totalX = 0
        totalNums = 0

        # each group is evaluated everytime
        # as it appears in the equation
        for c, x, num, isEq in re.findall(r'([+-]?\d*)(x)|([+-]?\d*)|(=)', equation):

            if isEq:
                sign = -1

            elif x:

                if c == '' or c == '+':
                    c = 1

                elif c == '-':
                    c = -1

                totalX += sign * int(c)

            elif num:
                totalNums += sign * int(num)

        return f'x={-totalNums//totalX}' if totalX else 'No solution' if totalNums else 'Infinite solutions'


sol = Solution()

res = sol.solveEquation('x+5-3+x=6+x-2')
print(res)
