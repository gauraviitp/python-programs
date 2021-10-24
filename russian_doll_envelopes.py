from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda e: -e[1])  # descending on height
        envelopes.sort(key=lambda e: e[0])  # ascending on width

        s = []  # sorted list

        for env in envelopes:
            i = bisect_left(s, env[1])

            if i == len(s):
                s.append(env[1])
            else:
                s[i] = env[1]

        return len(s)
