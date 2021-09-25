class Solution:
    def convertRoman(self, n):
        # Code here

        l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        d = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
             90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

        res = []

        i = 0
        while n > 0:

            while n >= l[i]:

                res += [d[l[i]]]

                n -= l[i]

            i += 1

        return ''.join(res)


sol = Solution()
sol.convertRoman(5)
