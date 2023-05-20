from collections import defaultdict, deque


# create adjacency list for graph using edges
def adjacencySet(edges):
    adjacency_dict = defaultdict(list)
    for x, y in edges:
        adjacency_dict[x].append(y)
        if len(adjacency_dict[y]) == 0:
            adjacency_dict[y] = []
    return adjacency_dict


# using dfs to search a target in a graph
def dfs(target, graph, start, visited, res):
    visited.add(start)
    if start == target:
        res[0] = True
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(target, graph, neighbor, visited, res)


def dfs_out(target, graph):
    visited = set()
    res = [False]
    for node in graph:
        if node not in visited:
            dfs(target, graph, node, visited, res)
    return res[0]


# using a bfs to search a target in a graph
def bfs(target, graph, start, visited, res):
    node_list = deque()
    node_list.append(start)
    while len(node_list) > 0:
        size = len(node_list)
        for i in range(size):
            top = node_list.popleft()
            if top == target:
                res[0] = True
            for neighbor in graph[top]:
                if neighbor not in visited:
                    node_list.append(neighbor)
            visited.add(top)


def bfs_out(target, graph):
    visited = set()
    res = [False]
    for node in graph:
        if node not in visited:
            bfs(target, graph, node, visited, res)
    return res[0]


# assume the graph has no cycle
def topologicalSort(graph):
    in_degree_dict = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree_dict[neighbor] += 1
    zero_degree = []
    for node in in_degree_dict:
        if in_degree_dict[node] == 0:
            zero_degree.append(node)
    topological_order = []
    while len(zero_degree) > 0:
        node = zero_degree.pop()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree_dict[neighbor] -= 1
            if in_degree_dict[neighbor] == 0:
                zero_degree.append(neighbor)
    return topological_order


if __name__ == "__main__":
    # input_edges = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]
    input_edges = [(1, 2), (2, 3), (1, 3), (3, 2), (4, 5)]
    input_graph = adjacencySet(input_edges)
    print(input_graph)
    print(dfs_out(2, input_graph))
    print(dfs_out(4, input_graph))
    print(dfs_out(8, input_graph))
    print(bfs_out(2, input_graph))
    print(bfs_out(4, input_graph))
    print(bfs_out(8, input_graph))
    # create a graph with no cycle and output the topological ordering
    input_edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
    input_graph = adjacencySet(input_edges)
    print(input_graph)
    print(topologicalSort(input_graph))
