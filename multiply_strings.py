class Solution:
    def multiplyStrings(self, s1, s2):
        sign1 = 1
        sign2 = 1

        if s1 and s1[0] == '-':
            sign1 = -1
            s1 = s1[1:]

        if s2 and s2[0] == '-':
            sign2 = -1
            s2 = s2[1:]

        n1 = len(s1)
        n2 = len(s2)

        s = [0] * (n1 + n2)

        for i in range(n1-1, -1, -1):
            carry = 0
            for j in range(n2-1, -1, -1):

                num = s[i+j+1] + int(s1[i]) * int(s2[j]) + carry

                s[i+j+1] = num % 10
                carry = num//10
            s[i] = carry

        nonzero = -1

        for i in range(len(s)):
            if s[i] != 0:
                nonzero = i
                break

        if nonzero == -1:
            return '0'
        elif sign1 * sign2 == -1:
            return ''.join(['-'] + list(map(str, s[nonzero:])))
        else:
            return ''.join(map(str, s[nonzero:]))


sol = Solution()
print(sol.multiplyStrings('4416', '-333'))
