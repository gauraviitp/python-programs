# LC - 336
# palindrome_pairs.py

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        s = dict((word, i) for i, word in enumerate(words))

        def isPalindrome(x):
            return x == x[::-1]

        res = []
        for i, word in enumerate(words):
            n = len(word)

            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]

                # case 1
                if isPalindrome(prefix):
                    back = suffix[::-1]

                    if back != word and back in s:
                        res.append((s[back], i))

                # j == 0 for case 1 and
                # j == n for case 2 are the same cases
                if j != n and isPalindrome(suffix):
                    front = prefix[::-1]

                    if front != word and front in s:
                        res.append((i, s[front]))

        return res
