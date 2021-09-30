# User function Template for python3
from collections import deque, defaultdict


class Solution:

    # Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root):
        # Your code here

        q = deque([(root, 0)])

        d = defaultdict(list)

        while q:

            node, x = q.popleft()

            d[x].append(node.data)

            if node.left:
                q.append((node.left, x-1))

            if node.right:
                q.append((node.right, x+1))

        res = []

        for key in sorted(d):
            res.extend(d[key])

        return res
