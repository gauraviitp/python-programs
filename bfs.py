from collections import deque


class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q = deque([0])
        visited = set()

        res = []

        while q:

            u = q.popleft()
            res.append(u)

            for v in adj[u]:
                if v not in visited:
                    q.append(v)
                    visited.add(v)

        return res
