
class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array of distinct elements
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''

        if l > r:
            return -1

        m = (l+r)//2

        arr[r], arr[m] = arr[m], arr[r]

        i = l

        for j in range(l, r):
            if arr[j] < arr[r]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[r] = arr[r], arr[i]

        if i == k-1:
            return arr[i]

        if k > i:
            l = i+1
        else:
            r = i-1

        return self.kthSmallest(arr, l, r, k)


sol = Solution()
print(sol.kthSmallest([7, 10, 4, 3, 20, 15], 0, 5, 3))
