from collections import deque

# Function to return a list containing the level order traversal in spiral form.


def findSpiral(root):
    # Code here

    if not root:
        return []

    q = deque([root])

    level = 1

    res = []

    while q:

        n = len(q)

        for _ in range(n):

            if level & 1 == 1:
                node = q.pop()
                res.append(node.data)

                if node.right:
                    q.appendleft(node.right)

                if node.left:
                    q.appendleft(node.left)

            else:
                node = q.popleft()
                res.append(node.data)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        level += 1

    return res
