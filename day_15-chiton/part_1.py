import utils as u
import numpy as np

from collections import defaultdict


s = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

cave = np.array([[int(x) for x in l] for l in s.splitlines()])
cave = u.import_data("./data/input")

start_point = (0,0)
end_point = cave.shape[0]-1, cave.shape[1]-1
neighbors = lambda pos: u.get_adjacent_coordinates(cave, pos[0], pos[1])

"""
  Represent the cave matrix as a graph. We define the graph as a dictionary,
  an entry of which looks like
    graph[v0] = [(v1, d1), (v2, d2)]
  indicating that there is an edge between v0 and v1 with d1 distance, and an edge between v0 and v2 with d2 distance
"""
graph = {(i,j): [(n, cave[n]) for n in neighbors((i,j))] for i in range(cave.shape[0]) for j in range(cave.shape[1])}

"""
From: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. 
   The tentative distance of a node v is the length of the shortest path discovered so far between the node v and the starting node. 
   Since initially no path is known to any other vertex than the source itself (which is a path of length zero), all other tentative 
   distances are initially set to infinity. Set the initial node as current.

3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node. 
   Compare the newly calculated tentative distance to the current assigned value and assign the smaller one. 
   For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2, 
   then the distance to B through A will be 6 + 2 = 8. 
   If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.

4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it 
   from the unvisited set. A visited node will never be checked again.

5. If the destination node has been marked visited (when planning a route between two specific nodes) 
   or if the smallest tentative distance among the nodes in the unvisited set is infinity 
   (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes), 
   then stop. The algorithm has finished.

6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, 
   and go back to step 3.
"""

unvisited_nodes = set(v for v in graph)

tentative_distance_values = {v: np.Inf for v in graph}
tentative_distance_values[start_point] = 0

previous_node = {v: None for v in graph}

current_node = start_point
while unvisited_nodes:
    for neigh,d in graph[current_node]:
        if neigh in unvisited_nodes:
            new_distance = tentative_distance_values[current_node] + d
            if new_distance < tentative_distance_values[neigh]:
                tentative_distance_values[neigh] = new_distance
                previous_node[neigh] = current_node              

    unvisited_nodes.remove(current_node)
    current_node = u.find_unvisited_node_with_smallest_tentative_distance(unvisited_nodes, tentative_distance_values)


print(tentative_distance_values[end_point])
