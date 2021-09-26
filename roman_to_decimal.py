class Solution:
    def romanToDecimal(self, S):
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}

        n = len(S)
        i = 0

        res = 0
        while i < n:
            if i + 1 < n and S[i:i+2] in d:
                res += d[S[i:i+2]]
                i += 2
            else:
                res += d[S[i:i+1]]
                i += 1

        return res
