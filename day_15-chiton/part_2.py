from numpy.core.fromnumeric import size
import utils as u
import numpy as np

import heapq as hq


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

#cave = np.array([[int(x) for x in l] for l in s.splitlines()])
cave = u.import_data("./data/input")

tile = cave.copy()

nr, nc = cave.shape

for i in range(1,5):
  tile = tile+1
  tile[tile==10]=1
  cave = np.concatenate([cave, tile], axis=1)

tile = cave.copy()
nr, nc = cave.shape
for i in range(1,5):
  tile = tile+1
  tile[tile>9]=1
  cave = np.concatenate([cave, tile], axis=0)


neighbors = lambda pos: u.get_adjacent_coordinates(cave, pos[0], pos[1])

start_point = (0,0)
end_point = cave.shape[0]-1, cave.shape[1]-1


"""
  Represent the cave matrix as a graph. We define the graph as a dictionary,
  an entry of which looks like
    graph[v0] = [(v1, d1), (v2, d2)]
  indicating that there is an edge between v0 and v1 with d1 distance, and an edge between v0 and v2 with d2 distance
"""
graph = {(i,j): [(n, cave[n]) for n in neighbors((i,j))] for i in range(cave.shape[0]) for j in range(cave.shape[1])}

visited = set()

costs = {v: np.Inf for v in graph}
costs[start_point] = 0

queue = [(costs[start_point], start_point)]


while queue:
    current_cost , current_node = hq.heappop(queue)
    #if current_node in visited:
    #    continue

    for neigh,d in graph[current_node]:
        if neigh not in visited:
            new_cost = costs[current_node] + d
            if new_cost < costs[neigh]:
                costs[neigh] = new_cost
                hq.heappush(queue, (new_cost, neigh)) 
    visited.add(current_node)

print(costs[end_point])
