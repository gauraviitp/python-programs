# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:

    def KDistanceNodes(self, root, target, k):
        # code here
        # return the sorted list all nodes at k distance from target

        res = []

        def find(node, depth):
            if not node or depth < 0:
                return

            if depth == 0:
                res.append(node.data)
                return

            find(node.left, depth-1)
            find(node.right, depth-1)

        def recurse(node):
            if not node:
                return -1

            if node.data == target:
                find(node, k)
                return 0

            left = recurse(node.left)
            if left != -1:
                if left + 1 == k:
                    res.append(node.data)
                else:
                    find(node.right, k-left-2)

                return left + 1

            right = recurse(node.right)
            if right != -1:
                if right + 1 == k:
                    res.append(node.data)
                else:
                    find(node.left, k-right-2)

                return right + 1

            return -1

        recurse(root)
        return list(sorted(res))
