
import collections
import sys

sys.setrecursionlimit(2 * 10**8)

sys.stdin = open(f'Kickstart\\2020_D_BeautyOfTree_input.txt')
sys.stdout = open(f'Kickstart\\2020_D_BeautyOfTree_output.txt', 'w')


def read_ints():
    return map(int, input().split())


def dfs(graph, root, path, visits, k):

    path.append(root)

    for child in graph[root]:
        dfs(graph, child, path, visits, k)

    path.pop()

    # Start the visit at the current node.
    visits[root] += 1

    # Every kth node can have visits[root] number of visits.
    # for node in path[-k::-k]:
    #    visits[node] += 1

    # Or you can just update the kth node from the end.
    # 2*kth node will be updated when kth node is the root.
    if k <= len(path) and path[-k]:
        visits[path[-k]] += visits[root]


def solve_beauty_of_tree():

    t, = read_ints()

    for test_case in range(1, t+1):

        n, a, b = read_ints()

        parents = list(read_ints())

        graph = collections.defaultdict(list)

        for i in range(len(parents)):
            graph[parents[i]].append(i+2)

        visits_a = [0] * (n + 1)
        visits_b = [0] * (n + 1)

        dfs(graph, 1, [], visits_a, a)
        dfs(graph, 1, [], visits_b, b)

        expected_value = 0

        for i in range(1, n+1):
            expected_value += (visits_a[i] + visits_b[i] -
                               visits_a[i] * visits_b[i] / n)

        print(f'Case #{test_case}: {expected_value / n}')


if __name__ == '__main__':
    solve_beauty_of_tree()
