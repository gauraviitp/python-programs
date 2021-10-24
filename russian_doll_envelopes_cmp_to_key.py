import functools
from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        def compare(env1, env2):
            if env1[0] == env2[0]:
                return env2[1] - env1[1]  # descending on height
            else:
                return env1[0] - env2[0]  # ascending on width

        envelopes.sort(key=functools.cmp_to_key(compare))

        s = []  # sorted list

        for env in envelopes:
            i = bisect_left(s, env[1])

            if i == len(s):
                s.append(env[1])
            else:
                s[i] = env[1]

        return len(s)
