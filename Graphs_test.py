import Graphs
from  math import inf

def bfs_test():
    graph = []
    graph.append([2])
    graph.append([2])
    graph.append([0, 1])
    p = [-1 for i in range(len(graph))]
    Graphs.bfs(graph, p, 0)
    assert p[0] == -1 and p[1] == 2 and p[2] == 0, "Incorrect solution"

def bfs_adj_vertex_test():
    graph = []
    graph.append([0, 0, 1])
    graph.append([0, 0, 1])
    graph.append([1, 1, 0])
    p = [-1 for i in range(len(graph))]
    Graphs.bfs_adj_vertex(graph, p, 0)
    assert p[0] == -1 and p[1] == 2 and p[2] == 0, "Incorrect solution"

def dfs_test():
    graph = []
    graph.append([2, 1])
    graph.append([2])
    graph.append([0, 1])
    p = [-1 for i in range(len(graph))]
    color = [0] * len(graph)
    timers = [[0 for j in range(2)] for i in range((len(graph)))]
    timer = [0]
    Graphs.dfs(graph, 0, p, color, timers, timer)
    assert p[0] == -1 and p[1] == 2 and p[2] == 0, "Incorrect solution"

def djikstra_sparse_test():
    graph = []
    graph.append([(1, 10), (2, 5), (3, 7)])
    graph.append([(0, 10), (4, 10), (5, 1)])
    graph.append([(0, 5), (4, 1), (5, 15)])
    graph.append([(0, 7), (4, 10)])
    graph.append([(1, 10), (2, 1)])
    graph.append([(1, 1), (2, 15)])
    p = [-1 for i in range(len(graph))]
    d = [inf] * len(graph)
    Graphs.djikstra_sparse(graph, 0, p, d)
    assert p[0] == -1 and p[1] == 0 and p[2] == 0 and p[3] == 0 and p[4] == 2 and p[5] == 1, "Incorrect solution"

def bellman_ford_shortest_path_test():
    graph = []
    graph.append([(0, 1, 10), (0, 2, 5), (0, 3, 7)])
    graph.append([(1, 0, 10), (1, 4, 10), (1, 5, 1)])
    graph.append([(2, 0, 5), (2, 4, 1), (2, 5, 15)])
    graph.append([(3, 0, 7), (3, 4, 10)])
    graph.append([(4, 1, 10), (4, 2, 1)])
    graph.append([(5, 1, 1), (5, 2, 15)])
    p = [-1 for i in range(len(graph))]
    d = [inf] * len(graph)
    Graphs.bellman_ford_shortest_path(graph, 0, p, d)
    assert p[0] == -1 and p[1] == 0 and p[2] == 0 and p[3] == 0 and p[4] == 2 and p[5] == 1, "Incorrect solution"

def bellman_ford_negative_cycle_test():
    graph = []
    graph.append([(0, 1, 5)])
    graph.append([(1, 2, 10)])
    graph.append([(2, 3, -20)])
    graph.append([(3, 0, 2)])
    path = []
    res = Graphs.bellman_ford_negative_cycle(graph, 0, path)
    assert res and path.index(0) != -1 and path.index(1) != -1 and path.index(2) != -1 and path.index(3) != -1, "Incorrect solution" 

def floyd_warshall_test():
    d = [
            [inf, 10, 5, 7, inf, inf],
            [inf, inf, inf, inf, 10,  1],
            [inf, inf, inf, inf, 3,  inf],
            [inf, inf, inf, inf, inf, 1],
            [inf, inf, inf, inf, inf, inf],
            [inf, inf, inf, inf, inf, inf]
        ]
    Graphs.floyd_warshall_algorithm(d)
    assert d[0][1] == 10 and d[0][2] == 5 and d[0][3] == 7 and d[0][4] == 8 and d[0][5] == 8, "Incorrect solution"

def kruskals_minimum_spanning_tree_test():
    pass

def main():
    bfs_test()
    bfs_adj_vertex_test()
    dfs_test()
    djikstra_sparse_test()
    bellman_ford_shortest_path_test()
    bellman_ford_negative_cycle_test()
    floyd_warshall_test()

if __name__ == '__main__':
    main()