# Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    # Code here

    if not root:
        return []

    q = []
    s = [root]

    level = 1

    res = []

    while q or s:

        if level & 1 == 1:
            while s:
                node = s.pop()
                res.append(node.data)

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)

        else:
            while q:
                node = q.pop()
                res.append(node.data)

                if node.left:
                    s.append(node.left)

                if node.right:
                    s.append(node.right)

        level += 1

    return res
