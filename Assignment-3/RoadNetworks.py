"""
In some states, it is not possible to drive between any two towns because they are not connected
 to the same road network.
Given a list of towns and a list of pairs representing roads between towns, return the number of
road networks.
(For example, a state in which all towns are connected by roads has 1 road network,
and a state in which none of the towns are connected by roads has 0 road networks.)

time complexity O(n + m), n refer to towns and m refer to roads
space complexity O(n + m), n refer to towns and m refer to roads
time spent on the question: about 20 min
"""
from collections import defaultdict


# use dfs to traverse all roads of a town
def dfs(graph, start, visited):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# build adjacency list of the graph
def build_graph(edges):
    graph = defaultdict(list)
    for town1, town2 in edges:
        graph[town1].append(town2)
        graph[town2].append(town1)
    return graph


def RoadNetworks(towns, roads):
    if len(roads) == 0:
        return 0
    adjacency_list = build_graph(roads)
    num_of_networks = 0
    visited = set()
    # traverse all towns to find number of networks
    for town in adjacency_list:
        if town not in visited:
            dfs(adjacency_list, town, visited)
            num_of_networks += 1
    return num_of_networks


if __name__ == "__main__":
    input_towns = ["Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth", "Glacier Bay", "Fairbanks", "McCarthy",
                   "Copper Center", "Healy"]
    input_roads = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"),
                   ("Anchorage", "Copper Center"),
                   ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
    print(RoadNetworks(input_towns, input_roads))
