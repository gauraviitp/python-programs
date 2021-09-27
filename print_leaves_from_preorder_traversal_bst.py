# Print leaf nodes from preorder traversal of BST

class Solution:
    def leafNodes(self, arr, N):

        res = []

        def recurse(i, j):

            if i + 1 == j:
                res.append(arr[i])
                return

            if i == j:
                return

            val = arr[i]

            k = i + 1

            while k < j and arr[k] <= val:
                k += 1

            recurse(i+1, k)
            recurse(k, j)

        recurse(0, len(arr))

        return res


sol = Solution()
print(sol.leafNodes([3, 2, 4], 3))
