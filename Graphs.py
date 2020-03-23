from sys import stdin as istream
from sys import stdout as ostream
from collections import deque
from math import inf
import heapq

def bfs(adj: "list of list", p: list, s: int):
    n = len(adj)
    used = [False] * n
    d = [0] * n
    q = deque()
    
    q.append(s)
    p[s] = -1
    used[s] = True

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not used[v]: # first time you discover, mark the vertex as used
                used[v] = True
                d[v] = d[u] + 1
                p[v] = u
                q.append(v)

def bfs_adj_vertex(adj: 'list of list', p: list, s: int):
    n = len(adj)
    q = deque()
    d = [0] * n
    used = [False] * n

    used[s] = True
    p[s] = -1
    q.append(s)

    while q:
        u = q.popleft()
        for v in range(n):
            if adj[u][v] > 0:
                if not used[v]:
                    used[v] = True
                    d[v] = d[u] + 1
                    p[v] = u
                    q.append(v)

def dfs(adj: 'list of list', s: int, p: list, color: list, times: 'list of list', timer: list):
    timer[0] += 1
    times[s][0] = timer[0] # time of entry
    color[s] = 1 # visiting
    for v in adj[s]:
        if color[v] == 0: # not yet visiting or visited
            p[v] = s
            dfs(adj, v, p, color, times, timer)
    color[s] = 2
    timer[0] += 1 # time of exit
    times[s][1] = timer[0]

def djikstra_sparse(adj: 'list of edges', s: int, p: list, d: list):
    d[s] = 0
    p[s] = -1
    heap = [(0, s)]

    while heap:
        dist_u, u = heapq.heappop(heap)
        if dist_u != d[u]:
            continue
        for v, dist in adj[u]:
            if d[u] + dist < d[v]: # new shortest path is found to v via u
                p[v] = u
                d[v] = d[u] + dist
                heapq.heappush(heap, (d[v], v))

def bellman_ford_shortest_path(adj: 'list of edges', s: int, p: list, d: list):
    n = len(adj)
    d = [inf] * n
    d[s] = 0
    for _ in range(n - 1):  
        any = False
        for i in range(n):  
            for u, v, weight in adj[i]:
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    p[v] = u
                    any = True
        if not any:
            break

def bellman_ford_negative_cycle(adj: 'list of edges', s: int, path: list):
    n = len(adj)
    d = [inf] * n
    p = [-1] * n
    d[s] = 0
    x = -1
    for _ in range(n):  
        x = -1
        for i in range(n):  
            for u, v, weight in adj[i]:
                if d[u] + weight < d[v]:
                    d[v] = d[u] + weight
                    p[v] = u
                    x = v
    if x != -1:
        y = x # x is either in the cycle or accessible from it
        for i in range(n):
            y = p[y]
        cur = y
        while True:
            path.append(cur)
            if cur == y and len(path) > 0:
                break
            cur = p[cur]
        path.reverse()




        return True
    else:
        return False