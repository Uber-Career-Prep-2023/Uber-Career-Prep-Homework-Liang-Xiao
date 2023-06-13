"""
Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length
of the shortest path from the origin to the destination in which the edges traversed alternate in color.
Return -1 if no such path exists.

time complexity O(n), n refer to edges
space complexity O(n), n refer to nodes
time spent on the question: about 30 min
"""
from collections import defaultdict, deque


# using bfs to find the shortest path
def bsf(origin, destination, graph, color):
    queue = [(origin, color)]
    visited = set()
    level = 0
    while queue:
        next_q = []
        for item in queue:
            visited.add(item)
            node, color = item
            if node == destination:
                return level
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor[1] != color:
                    next_q.append(neighbor)
        queue = next_q
        level += 1
    return -1


def AlternatingPath(origin, destination, edges):
    # construct adjacency list of the graph and color set
    color_set = set()
    adjacency_list = defaultdict(list)
    for point_x, point_y, color in edges:
        adjacency_list[point_x].append((point_y, color))
        color_set.add(color)

    # compare result of 2 options
    color1, color2 = color_set
    num_of_red = bsf(origin, destination, adjacency_list, color1)  # begin with red color
    num_of_blue = bsf(origin, destination, adjacency_list, color2)  # begin with blue color
    if num_of_red == -1 and num_of_blue == -1:
        return -1
    if num_of_red == -1 or num_of_blue == -1:
        return num_of_blue if num_of_red == -1 else num_of_red
    return min(num_of_red, num_of_blue)


if __name__ == "__main__":
    input_edges = [('A', 'B', "blue"), ('A', 'C', "red"), ('B', 'D', "blue"), ('B', 'E', "blue"), ('C', 'B', "red"),
                   ('D', 'C', "blue"), ('A', 'D', "red"),
                   ('D', 'E', "red"), ('E', 'C', "red")]
    input_origin = 'A'
    input_destination = 'E'
    print(AlternatingPath(input_origin, input_destination, input_edges))
    input_origin = 'E'
    input_destination = 'D'
    print(AlternatingPath(input_origin, input_destination, input_edges))
    print(AlternatingPath('B', 'C', input_edges))
