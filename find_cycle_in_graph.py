class Solution:

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here

        def dfs(u, color):
            color[u] = 1

            for v in adj[u]:
                if color[v] == 1:
                    return
                elif color[v] == 0:
                    dfs(v, color)

            color[u] = 2

        color = [0] * V
        for u in range(V):
            if color[u] == 0:
                dfs(u, color)

        return any(val == 1 for val in color)
