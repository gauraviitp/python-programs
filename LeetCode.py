from collections import Counter
import heapq

"""
    1296 - Divide array in sets of k consecutive numbers
"""

def isPossibleDivide(nums: list, k: int):
    ct = {}
    for i in nums: ct[i] = ct.get(i, 0) + 1
    for i in sorted(ct):
        t = ct[i]
        if t <= 0: continue
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
        self.heap_first_half = [] # a max heap
        self.heap_second_half = [] # a min heap

    def addNum(self, num):
        min_second = heapq.heappushpop(self.heap_second_half, num)
        heapq.heappush(self.heap_first_half, - min_second)
        if len(self.heap_first_half) - len(self.heap_second_half) > 1:
            heapq.heappush(self.heap_second_half, - heapq.heappop(self.heap_first_half))

    def findMedian(self):
        if len(self.heap_first_half) > len(self.heap_second_half):
            return - self.heap_first_half[0]
        else:
            return (- self.heap_first_half[0] + self.heap_second_half[0]) / 2

"""
    609 - Find Duplicate File in System
"""

def find_duplicate_groups(files: list):
    pass


