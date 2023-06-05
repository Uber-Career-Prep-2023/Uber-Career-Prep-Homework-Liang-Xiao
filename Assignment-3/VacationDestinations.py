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


def VacationDestinations(destinations, origin, k):
    # create adjacency_list of the graph
    adjacency_list = defaultdict(list)
    for city1, city2, distance in destinations:
        adjacency_list[city1].append((city2, distance))
        adjacency_list[city2].append((city1, distance))
    # initiate the distance of origin to 0 and others to infinity
    # put the origin in priority queue
    distances_dict = {}
    priority_queue = []
    for city in adjacency_list:
        if city == origin:
            distances_dict[city] = 0
            priority_queue.append([0, city])
        else:
            distances_dict[city] = float('inf')

    # use dijkstra algorithm to find the cities with the shortest path less or equal than k
    visited_city = set()
    arrived_destination = []
    while len(priority_queue) > 0:
        city = heapq.heappop(priority_queue)[-1]
        visited_city.add(city)
        cur_distance = distances_dict[city]
        if 0 < cur_distance <= k:
            arrived_destination.append(city)
        for neighbour, distance in adjacency_list[city]:
            update = cur_distance + distance
            if city != origin:
                update += 1  # a stopover in a city adds an hour of travel time.
            if neighbour not in visited_city and distances_dict[neighbour] > update:
                distances_dict[neighbour] = update
            if neighbour not in visited_city:
                heapq.heappush(priority_queue, [distances_dict[neighbour], neighbour])
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
