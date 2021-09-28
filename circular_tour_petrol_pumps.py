'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''


class Solution:

    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        start = 0

        s = 0

        d = 0

        for i in range(n):

            s += lis[i][0] - lis[i][1]

            if s < 0:
                start = i+1
                d += s

                s = 0

        return start if s + d >= 0 else -1
