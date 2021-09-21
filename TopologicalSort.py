import sys
import collections
from sys import setrecursionlimit

setrecursionlimit(2 * 10**6)

sys.stdin = open(f'input.txt')
sys.stdout = open(f'output.txt', 'w')


class CycleError(Exception):
    pass


def read():
    return list(map(int, input().split()))


def dfs(u, g, color, stack):

    color[u] = 1  # visiting

    for v in g[u]:

        if color[v] == 0:
            dfs(v, g, color, stack)
        elif color[v] == 1:
            raise CycleError('cycle detected')

    color[u] = 2  # visited
    stack.append(u)


def topological_sort(g):

    stack = []
    color = collections.defaultdict(int)

    try:
        for u in g.keys():

            if color[u] == 0:
                dfs(u, g, color, stack)

        return 1, reversed(stack)

    except CycleError:
        return -1, []


def solve():
    t,  = read()

    for testCase in range(1, t+1):

        r, c = read()

        grid = []

        for _ in range(r):
            grid.append(list(input()))

        g = {}

        for i in range(r-2, -1, -1):
            for j in range(c):

                if grid[i+1][j] not in g:
                    g[grid[i+1][j]] = set()

                if grid[i][j] not in g:
                    g[grid[i][j]] = set()

                if grid[i+1][j] != grid[i][j]:
                    g[grid[i+1][j]].add(grid[i][j])

        if r == 1:
            for u in set(grid[0]):
                g[u] = set()

        ok, res = topological_sort(g)

        print(f'Case #{testCase}: {-1 if ok == -1 else "".join(res)}')


solve()
