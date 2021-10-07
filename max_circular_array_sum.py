from math import inf

# Complete this function
# Function to find maximum circular subarray sum.


def circularSubarraySum(arr, n):
    # Your code here

    def kadane(a):
        maxSum = -inf
        curSum = 0

        for val in a:
            curSum += val
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0

        return maxSum

    maxFromWrap = sum(arr) + kadane(list(map(lambda x: -x, arr)))
    maxFromKadane = kadane(arr)

    if maxFromWrap != 0:
        return max(maxFromKadane, maxFromWrap)
    else:
        return maxFromKadane
