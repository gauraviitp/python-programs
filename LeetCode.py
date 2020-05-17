from collections import Counter
import heapq

"""
    1296 - Divide array in sets of k consecutive numbers
"""


def isPossibleDivide(nums: list, k: int):
    ct = {}
    for i in nums:
        ct[i] = ct.get(i, 0) + 1
    for i in sorted(ct):
        t = ct[i]
        if t <= 0:
            continue
        for j in range(k):
            if i + j not in ct or ct[i + j] < t:
                return False
            ct[i + j] -= t
            if ct[i] < 0:
                return False
    return True


"""
    295 - Find Median from Data Stream
"""


class MedianFinder:
    def __init__(self):
        self.heap_first_half = []  # a max heap
        self.heap_second_half = []  # a min heap

    def addNum(self, num):
        min_second = heapq.heappushpop(self.heap_second_half, num)
        heapq.heappush(self.heap_first_half, - min_second)
        if len(self.heap_first_half) - len(self.heap_second_half) > 1:
            heapq.heappush(self.heap_second_half, -
                           heapq.heappop(self.heap_first_half))

    def findMedian(self):
        if len(self.heap_first_half) > len(self.heap_second_half):
            return - self.heap_first_half[0]
        else:
            return (- self.heap_first_half[0] + self.heap_second_half[0]) / 2


"""
    768 - Max chunks to make sorted II
"""


def maxChunksToSorted(arr: list):
    n = len(arr)
    max_left = [0] * n
    cur_max = arr[0]
    for i in range(n):
        cur_max = max(cur_max, arr[i])
        max_left[i] = cur_max
    min_right = [0] * n
    cur_min = arr[n - 1]
    for i in range(n - 1, -1, -1):
        cur_min = min(cur_min, arr[i])
        min_right[i] = cur_min

    res = 1
    for i in range(n - 1):
        if max_left[i] <= min_right[i + 1]: # elements to the left can be sorted 
            res += 1

    return res


"""
    769 - Max chunks to make sorted
"""

def maxChunksToSorted_I(arr: list):
    max_left = arr[0]
    ans = 0
    for i in range(len(arr)):
        max_left = max(max_left, arr[i])
        if max_left == i: # elements upto this point can be sorted
            ans += 1
    return ans


"""
    416 - Partition Equal Subset Sum
"""

def partition_equal_subset_sum(nums: list): 
    sum_val = 0
    bit_set = 1
    for num in nums:
        sum_val += num
        bit_set |= bit_set << num
    return sum_val & 1 == 0 and (bit_set >> (sum_val // 2) & 1)


"""
    
"""

