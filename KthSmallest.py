# User function Template for python3
from heapq import heapify, heappush, heappushpop


class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''

        heap = []

        for i in range(k):
            heappush(heap, -arr[i])

        for i in range(k, len(arr)):
            if arr[i] < -heap[0]:
                heappushpop(heap, -arr[i])

        return -heap[0]
