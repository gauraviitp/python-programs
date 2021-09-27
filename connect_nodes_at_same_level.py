from collections import deque


class Solution:
    # Function to connect nodes at same level.
    def connect(self, root):
        q = deque([root])

        while q:

            n = len(q)
            right = None

            for i in range(n):
                node = q.popleft()
                node.nextRight = right

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

                right = node

        return root
