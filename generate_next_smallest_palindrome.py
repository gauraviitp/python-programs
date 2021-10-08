class Solution:

    def generateNextPalindrome(self, num, n):

        if all(val == 9 for val in num):
            for i in range(n-1):
                num[i] = 0
            num[n-1] = 1
            num.insert(0, 1)
        return num

        incr = False

        lo = n//2 if n & 1 == 1 else n//2 - 1
        hi = n//2

        while lo >= 0 and num[lo] == num[hi]:
            lo -= 1
            hi += 1

        if lo < 0 or hi >= n:  # palindrome
            lo = n//2 - 1  # point to mid left
            hi = n//2  # point to mid right

        # copying from left to right
        # is not going to be enough
        # as left number is less than equal
        # to number on right

        # increment must start from the middle numbers
        if num[lo] <= num[hi]:
            lo = n//2 if n & 1 else n//2 - 1
            hi = n//2
            incr = True

        c = 0
        while incr:
            num[lo] += 1
            c = num[lo] // 10
            num[lo] = num[lo] % 10
            num[hi] = num[lo]

            if c == 0:
                break
            lo -= 1
            hi += 1

        while lo >= 0:
            num[hi] = num[lo]

            lo -= 1
            hi += 1

        return num
