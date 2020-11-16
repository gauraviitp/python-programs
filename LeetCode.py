import math
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq

from Algebra import factorization_trial_division

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
        if max_left[i] <= min_right[i + 1]:  # elements to the left can be sorted
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
        if max_left == i:  # elements upto this point can be sorted
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
            if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
                continue
            if (x1, y1) in used:
                continue
            cost = 1
            if grid[x][y] == 1 and (dx, dy) == (0, 1) or \
               grid[x][y] == 2 and (dx, dy) == (0, -1) or \
               grid[x][y] == 3 and (dx, dy) == (1, 0) or \
               grid[x][y] == 4 and (dx, dy) == (-1, 0):
                cost = 0
            node = ((x1, y1), dist + cost)
            if cost == 0:
                q.appendleft(node)
            else:
                q.append(node)
    return dist


"""
1354. Construct Target Array With Multiple Sums
"""


def isPossibleToConstructTargetArray(self, target: 'List[int]'):
    total = sum(target)
    for i in range(len(target)):
        target[i] = -target[i]
    import heapq
    heapq.heapify(target)
    while True:
        hi = -heapq.heappop(target)
        rest = total - hi
        # print(hi, rest, total)
        if hi == 1 or rest == 1:
            return True
        if rest >= hi or rest == 0:
            return False
        hi = hi % rest
        if hi == 0:
            return False
        total = rest + hi
        heapq.heappush(target, -hi)
    return False


class MinRefuelStops:
    def minRefuelStops(self, target: int, startFuel: int, stations: 'List[List[int]]') -> int:
        import heapq
        dist = startFuel
        i = 0
        q = []
        res = 0
        while True:
            while i < len(stations) and stations[i][0] <= dist:
                heapq.heappush(q, -stations[i][1])
                i += 1
            if dist >= target:
                return res
            if not q:
                return -1
            dist += -heapq.heappop(q)
            res += 1
        return res


class MinRefuelStopsDp:
    def minRefuelStops(self, target: int, startFuel: int, stations: 'List[List[int]]') -> int:
        n = len(stations)
        # dp[t] is farthest distance we can have with t times of re-fueling
        dp = [0]*(n+1)
        dp[0] = startFuel  # by def
        for i in range(n):
            t = i+1
            while t >= 1 and dp[t-1] >= stations[i][0]:
                dp[t] = max(dp[t], dp[t-1]+stations[i][1])
                t -= 1
        i = 0
        while i <= n:
            if dp[i] >= target:
                return i
            i += 1
        return -1


class LargestDivisibleSubset:
    def largestDivisibleSubset(self, nums):
        sets = []
        nums.sort(reverse=True)
        for i in range(len(nums)):
            sets.append({nums[i]})
            set_to_merge = set()
            for d in range(i):
                if nums[d] % nums[i] == 0:
                    if len(sets[d]) > len(set_to_merge):
                        set_to_merge = sets[d]
            sets[i] |= set_to_merge
        return list(max(sets, key=len))


class MinSumOfLengths:
    def minSumOfLengths(self, arr, target: int) -> int:
        n = len(arr)
        res = []
        lo, hi, s = 0, 1, arr[0]
        while lo < n and (hi < n or s == target):
            while hi < n and s < target:
                s += arr[hi]
                hi += 1
            if s == target:
                res.append([lo, hi-1])
                s -= arr[lo]
                lo += 1
            while s > target and lo < hi:
                s -= arr[lo]
                lo += 1
            hi = max(lo, hi)
        okay = False
        res.sort(key=lambda x: x[1] - x[0] + 1)
        if len(res) < 2:
            return -1
        ans = res[0][1]-res[0][0]+1
        for i in range(1, len(res)):
            if res[i][0] > res[0][1] or res[i][1] < res[0][0]:
                ans += res[i][1]-res[i][0]+1
                okay = True
                break
        if okay:
            return ans
        else:
            return -1


class MaxVowels:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        res = 0
        j = 0
        for i in range(len(s)):
            while j < i+k and j < len(s):
                if s[j] in vowels:
                    count += 1
                res = max(res, count)
                j += 1
            if s[i] in vowels:
                count -= 1
        return res


class LongestOnes:
    def longestOnes(self, A, K: int) -> int:
        res = 0
        count = 0
        j = 0
        k = K
        for i in range(len(A)):
            while j < len(A) and (k > 0 or A[j] == 1):
                count += 1
                res = max(res, count)
                if A[j] == 0:
                    k -= 1
                j += 1
            if A[i] == 0:
                k += 1
            count -= 1
        return res


class AllPathsSourceTarget:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        paths = {}
        okay = [False]*n
        self.dfs(graph, 0, n, paths, okay)

    def dfs(self, graph, s, n, paths, okay):
        if s in paths:
            return
        if s == n-1:
            paths[s] = [[s]]
            okay[s] = True
            return
        paths[s] = []
        for t in graph[s]:
            if t not in paths:
                self.dfs(graph, t, n, paths, okay)
            if okay[t]:
                okay[s] = True
                for path in paths[t]:
                    l = path[:]
                    l.append(s)
                    paths[s].append(l)


class Node:
    def __init__(self, key=None, val=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def append(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail


class LRUCache:
    def __init__(self, capacity: int):
        self.list = LinkedList()
        self.hash = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.list.remove(node)
            self.list.append(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key].val = value
            return
        node = Node(key, value)
        self.hash[key] = node
        self.list.append(node)
        self.capacity += 1
        if self.capacity < 0:
            self.capacity += 1
            node = self.list.head.next
            self.list.remove(node)
            del self.hash[node.key]


class Graph:
    def __init__(self):
        import collections
        self.adj = collections.defaultdict(list)

    def add(self, u, v):
        self.adj[u].append(v)

    def topological_sort(self):
        q = []
        import collections
        used = collections.defaultdict(bool)

        def dfs(u):
            used[u] = True
            for v in self.adj[u]:
                if not used[v]:
                    dfs(v)
            q.append(u)
        for u in self.adj.keys():
            if not used[u]:
                dfs(u)
        return reversed(q)


class AlienDictionary:
    def solve(self, words):
        g = Graph()
        for i in range(0, len(words)-1):
            a, b = words[i], words[i+1]
            j = 0
            while j < len(a) and j < len(b) and a[j] == b[j]:
                j += 1
            if j < len(a) and j < len(b):
                g.add(a[j], b[j])
        return g.topological_sort()


class PalindromePartioningII:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [i-1 for i in range(n+1)]
        # print(cut)
        for i in range(n):
            j = 0
            while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
                cut[i+j+1] = min(cut[i+j+1], cut[i-j]+1)
                j += 1
            j = 0
            k = i+1
            while i-j >= 0 and k+j < n and s[i-j] == s[k+j]:
                cut[k+j+1] = min(cut[k+j+1], cut[i-j]+1)
                j += 1
        # print(cut)
        return cut[-1]


class RepeatedSubstrings:
    def findRepeatedDnaSequences(self, s: str):
        hashes = defaultdict(int)
        hash_sub = 0
        m, p = int(1e9+9), 31
        p_pow = (p**9) % m
        for c in range(10):
            hash_sub = hash_sub * p + (ord(s[c]) - ord('A') + 1)
            hash_sub = hash_sub % m
        hashes[hash_sub] += 1
        res = []
        for i in range(10, len(s)):
            hash_sub = (hash_sub - (ord(s[i-10]) - ord('A') + 1) * p_pow) % m
            hash_sub = (hash_sub * p + ord(s[i]) - ord('A') + 1) % m
            if hashes[hash_sub] == 1:
                res.append(s[i-9:i+1])
            hashes[hash_sub] += 1
        return res


class FindRightInterval:

    def search(self, intervals, k):

        lo, hi = 0, len(intervals)-1
        while lo < hi:
            mid = (lo+hi)//2
            if intervals[mid][0] < k:  # mid is less than k; k must be to the right
                lo = mid+1
            else:  # k is atleast mid
                hi = mid

        return intervals[lo][2] if lo >= 0 and intervals[lo][0] >= k else -1

    def findRightInterval(self, intervals):

        for i, interval in enumerate(intervals):
            interval.append(i)

        intervals.sort()

        res = [-1]*len(intervals)
        for i, interval in enumerate(intervals):
            res[interval[2]] = self.search(intervals, interval[1])

        return res


class MinimumWindowSubstring:
    def minWindow(self, s: str, t: str) -> str:

        start = end = 0

        head = 0
        d = math.inf  # length of min string

        # cnt is number of characters in the window [start, end]
        # that are in t as well
        # cnt never goes below 0

        cnt = len(t)
        cntT = Counter(t)

        while end < len(s):

            # process end
            if s[end] in cntT:
                # you have seen a char that is also in t
                if cntT[s[end]] > 0:
                    cnt -= 1
                cntT[s[end]] -= 1

            end += 1

            print(start, end, cnt, cntT, d, head)

            # process start
            while cnt == 0:
                if end - start < d:
                    head = start
                    d = end - start

                # if char at start is in t
                # and its count is zero
                if s[start] in cntT:
                    # you have seen a char
                    # which is in t
                    # and which will need to be seen again
                    if cntT[s[start]] == 0:
                        cnt += 1
                    cntT[s[start]] += 1

                start += 1

        if d == math.inf:
            return ""
        else:
            return s[head:head + d]


class FindAnagrams:
    def findAnagrams(self, s: str, p: str):
        P = Counter(p)

        res = []

        start = end = 0

        counter = len(p)

        while end < len(s):
            # process end

            if P[s[end]] > 0:
                counter -= 1
            P[s[end]] -= 1

            end += 1

            while counter == 0:
                res.append(start)

                if P[s[start]] == 0:
                    counter += 1

                P[s[start]] += 1

                start += 1

        return res
