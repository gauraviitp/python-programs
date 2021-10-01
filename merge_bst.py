
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''


class Solution:

    # Function to return a list of integers denoting the node
    # values of both the BST in a sorted order.
    def merge(self, root1, root2):
        # code here.

        def inorder(node):
            nonlocal pre
            nonlocal head

            if not node:
                return

            if node.left:
                inorder(node.left)

            if not head:
                head = node

            if pre:
                pre.right = node
                node.left = pre

            pre = node

            if node.right:
                inorder(node.right)

        pre = head = None
        inorder(root1)
        head1 = head

        pre = head = None
        inorder(root2)
        head2 = head

        res = []
        while head1 or head2:
            if head1 and head2:
                if head1.data <= head2.data:
                    res.append(head1.data)
                    head1 = head1.right
                else:
                    res.append(head2.data)
                    head2 = head2.right

            elif head1:
                res.append(head1.data)
                head1 = head1.right

            else:
                res.append(head2.data)
                head2 = head2.right

        return res
