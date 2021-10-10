class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.count = 1


class BinaryTree:

    def __init__(self):
        self.root = None

    def add(self, val):

        def insert(node):
            if node == None:
                return TreeNode(val)

            if val < node.val:
                node.left = insert(node.left)
            else:
                node.right = insert(node.right)
                node.count += 1

            return node

        self.root = insert(self.root)

    def find(self, val):

        def recurse(node):
            if node == None:
                return 0

            if node.val >= val:
                return 1 + recurse(node.left) + (node.right.count if node.right else 0)

            elif node.val < val:
                return recurse(node.right)

        return recurse(self.root)


class Solution:

    # [5,2,1,3,1]

    #5, [0, 0, 0, 0, 0], 5
    #2, [0, 0, 0, 1, 1], 4
    #1, [0, 1, 1, 1, 1], 3
    #3, [1, 1, 1, 1, 1], 5
    #1, [1, 1, 1, 2, 1], 3

    # we search how many elements are there in the sorted array
    # which are greater than or equal to 2*x + 1

    def reversePairs(self, nums) -> int:

        tree = BinaryTree()

        res = 0
        for num in nums:
            res += tree.find(2 * num + 1)

            tree.add(num)

        return res


sol = Solution()
print(sol.reversePairs([2, 4, 3, 5, 1]))
