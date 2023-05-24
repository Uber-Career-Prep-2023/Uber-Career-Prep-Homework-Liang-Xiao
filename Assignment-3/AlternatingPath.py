"""
Given an origin and a destination in a directed graph in which edges can be blue or red, determine the length
of the shortest path from the origin to the destination in which the edges traversed alternate in color.
Return -1 if no such path exists.

time complexity O(n + m), n refer to nodes and m refer to edges
space complexity O(n + m), n refer to nodes and m refer to edges
time spent on the question: about 30 min
"""
from collections import defaultdict, deque


# using bfs to find the shortest path
def bsf(origin, destination, graph, flag):
    shortest_path = 0
    queue = deque()
    queue.append(origin)
    stop = False
    while len(queue) > 0 and not stop:
        size = len(queue)
        if flag:  # alternating color using flag
            for i in range(size):
                node = queue.popleft()
                if node == destination:  # when reaching the target, change stop to terminate
                    stop = True
                    break
                for neighbour, color in graph[node]:
                    if color == "red":
                        queue.append(neighbour)
            if not stop:
                shortest_path += 1
            flag = not flag
        else:
            for i in range(size):
                node = queue.popleft()
                if node == destination:
                    stop = True
                    break
                for neighbour, color in graph[node]:
                    if color == "blue":
                        queue.append(neighbour)
            if not stop:
                shortest_path += 1
            flag = not flag
    if stop:
        return shortest_path
    return -1


def AlternatingPath(origin, destination, edges):
    # construct adjacency list of the graph
    adjacency_list = defaultdict(list)
    for point_x, point_y, color in edges:
        adjacency_list[point_x].append((point_y, color))
    # compare result of 2 options
    num_of_red = bsf(origin, destination, adjacency_list, True)  # begin with red color
    num_of_blue = bsf(origin, destination, adjacency_list, False)  # begin with blue color
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
