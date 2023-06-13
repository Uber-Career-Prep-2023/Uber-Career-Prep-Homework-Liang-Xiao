from collections import defaultdict, deque


# create adjacency list for graph using edges
def adjacencySet(edges):
    adjacency_dict = {}
    for x, y in edges:
        adjacency_dict[x] = []
        adjacency_dict[y] = []
    for x, y in edges:
        adjacency_dict[x].append(y)
    return adjacency_dict


# using dfs to search a target in a graph
def dfs(target, graph):
    visited = set()
    for node in graph:
        if node not in visited and dfs_helper(target, graph, node, visited):
            return True
    return False


def dfs_helper(target, graph, node, visited):
    if node == target:
        return True
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited and dfs_helper(target, graph, neighbour, visited):
            return True
    return False


# using a bfs to search a target in a graph
def bfs(target, graph, start, visited):
    node_list = deque()
    node_list.append(start)
    while len(node_list) > 0:
        current = node_list.popleft()
        visited.add(current)
        if current == target:
            return True
        for neighbour in graph[current]:
            if neighbour not in visited:
                node_list.append(neighbour)
    return False


def bfs_out(target, graph):
    visited = set()
    for node in graph:
        if node not in visited and bfs(target, graph, node, visited):
            return True
    return False


# assume the graph has no cycle
def topologicalSort(graph):
    # count the in degree of each node
    in_degree_dict = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree_dict[neighbor] += 1

    # find the nodes with 0 in degree
    zero_degree = []
    for node in in_degree_dict:
        if in_degree_dict[node] == 0:
            zero_degree.append(node)
    # pop nodes from zero degree list and update it
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
    print(dfs(2, input_graph))
    print(dfs(4, input_graph))
    print(dfs(8, input_graph))
    print(bfs_out(2, input_graph))
    print(bfs_out(4, input_graph))
    print(bfs_out(8, input_graph))
    # create a graph with no cycle and output the topological ordering
    input_edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
    input_graph = adjacencySet(input_edges)
    print(input_graph)
    print(topologicalSort(input_graph))
