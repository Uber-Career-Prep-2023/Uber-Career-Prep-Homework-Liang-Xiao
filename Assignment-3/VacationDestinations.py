"""
Given an origin city, a maximum travel time k, and pairs of destinations that can be reached directly from each other
with corresponding travel times in hours, return the number of destinations within k hours of the origin.
Assume that having a stopover in a city adds an hour of travel time.

time complexity O(m * log(n)), n refer to number of cities and m refer to number of paths
space complexity O(n + m), n refer to number of cities and m refer to number of paths
time spent on the question: about 2git0 min
"""
import heapq
from collections import defaultdict


# create adjacency_list of the graph

def build_graph(edges):
    graph = defaultdict(list)
    for city1, city2, distance in edges:
        graph[city1].append((city2, distance))
        graph[city2].append((city1, distance))
    return graph


def VacationDestinations(destinations, origin, k):
    adjacency_list = build_graph(destinations)

    # initiate the distance of origin to 0 and others to infinity
    # put the origin in priority queue
    distances_dict = {}
    priority_queue = []
    for city in adjacency_list:
        distances_dict[city] = float('inf')
    distances_dict[origin] = 0
    priority_queue.append((0, origin))

    # use dijkstra algorithm to find the cities with the shortest path less or equal than k
    visited_city = set()
    arrived_destination = []
    while priority_queue:
        city = heapq.heappop(priority_queue)[-1]
        visited_city.add(city)
        cur_distance = distances_dict[city]
        if 0 < cur_distance <= k:
            arrived_destination.append(city)
        for neighbour, distance in adjacency_list[city]:
            nei_distance = distances_dict[neighbour]
            update = cur_distance + distance
            if city != origin:
                update += 1  # a stopover in a city adds an hour of travel time.
            if nei_distance > update:
                nei_distance = update
                distances_dict[neighbour] = nei_distance
            if neighbour not in visited_city:
                heapq.heappush(priority_queue, [nei_distance, neighbour])
    return arrived_destination


if __name__ == "__main__":
    input_graph = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5),
                   ("Washington, D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5),
                   ("Philadelphia", "Washington, D.C.", 2.5)]
    origin_city = "New York"
    input_k = 5
    print(VacationDestinations(input_graph, origin_city, input_k))
    input_k = 7
    print(VacationDestinations(input_graph, origin_city, input_k))
    input_k = 8
    print(VacationDestinations(input_graph, origin_city, input_k))
