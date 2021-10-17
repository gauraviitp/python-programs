class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1:
            return str2

        n1 = len(str1)
        n2 = len(str2)

        if n1 > n2:
            return self.gcdOfStrings(str2, str1)

        if str2[:n1] == str1:
            return self.gcdOfStrings(str1, str2[n1:])
        else:
            return ""


sol = Solution()

sol.gcdOfStrings("ABABA", "AB")
