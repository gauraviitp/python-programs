class Solution:
    def merge(self, arr1, arr2, n, m):
        i = 0
        j = 0

        while i + j < n and j < m:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

        if j > 0:
            for k in range(j):
                arr1[n-1-k], arr2[k] = arr2[k], arr1[n-1-k]

        arr1.sort()
        arr2.sort()
