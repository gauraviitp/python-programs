
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

            if not node:
                return

            yield from inorder(node.left)

            yield node.data

            yield from inorder(node.right)

        head1 = inorder(root1)
        head2 = inorder(root2)

        cur1 = next(head1, None)
        cur2 = next(head2, None)

        res = []

        while cur1 or cur2:

            if cur1 and cur2:
                if cur1 <= cur2:
                    res.append(cur1)
                    cur1 = next(head1, None)
                else:
                    res.append(cur2)
                    cur2 = next(head2, None)

            elif cur1:
                res.append(cur1)
                cur1 = next(head1, None)

            elif cur2:
                res.append(cur2)
                cur2 = next(head2, None)

        return res
