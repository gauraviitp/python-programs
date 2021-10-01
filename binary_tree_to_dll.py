# User function Template for python3

class Node:
    """ Class Node """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Function to convert a binary tree to doubly linked list.


class Solution:
    def bToDLL(self, root):

        head = None
        pre = None

        def inorder(node):
            nonlocal pre
            nonlocal head

            if not node:
                return

            inorder(node.left)

            if not head:
                head = node

            if pre:
                pre.right = node
                node.left = pre

            pre = node

            inorder(node.right)

        inorder(root)

        return head
