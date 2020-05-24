from collections import Counter
from collections import deque
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
    1368 - Minimum cost to make at least one valid path in a grid 
"""
def minCost(self, grid: 'List[List[int]]') -> int:
        m, n = len(grid), len(grid[0])
        dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        q = deque()
        q.append(((0, 0), 0))
        used = set()
        dist = 0
        while q:
            u = q.popleft()
            x, y = u[0]
            used.add((x, y))
            dist = u[1]
            if (x, y) == (m-1, n-1):
                return dist
            for (dx, dy) in dirs:
                x1, y1 = x + dx, y + dy
                if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n: continue
                if (x1, y1) in used: continue
                cost = 1
                if grid[x][y] == 1 and (dx, dy) == (0, 1) or \
                   grid[x][y] == 2 and (dx, dy) == (0, -1) or \
                   grid[x][y] == 3 and (dx, dy) == (1, 0) or \
                   grid[x][y] == 4 and (dx, dy) == (-1, 0): cost = 0
                node = ((x1, y1), dist + cost)
                if cost == 0: q.appendleft(node)
                else: q.append(node)
        return dist

"""
1354. Construct Target Array With Multiple Sums
"""
def isPossibleToConstructTargetArray(self, target: 'List[int]'):
        total = sum(target)
        for i in range(len(target)): target[i] = -target[i]
        import heapq
        heapq.heapify(target)
        while True:
            hi = -heapq.heappop(target)
            rest = total - hi
            #print(hi, rest, total)
            if hi == 1 or rest == 1: return True
            if rest >= hi or rest == 0: return False
            hi = hi % rest
            if hi == 0: return False
            total = rest + hi
            heapq.heappush(target, -hi)
        return False

