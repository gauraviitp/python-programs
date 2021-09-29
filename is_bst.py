# User function Template for python3
import math


class Solution:

    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):

        def recurse(node, minVal, maxVal):
            if not node:
                return True

            return minVal < node.data < maxVal\
                and recurse(node.left, minVal, node.data)\
                and recurse(node.right, node.data, maxVal)

        return recurse(root, -math.inf, math.inf)
