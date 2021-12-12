import fileinput
from collections import defaultdict
from copy import deepcopy

def import_graph(path):
    edges = []
    for line in fileinput.input(path):
        line = line.rstrip()
        src, dst = line.split("-")
        edges.append((src,dst))
    return edges

    
def to_connections(graph):
    connections = defaultdict(set)
    for cave1, cave2 in graph:
        if not cave2 == "start" and not cave1=="end":
            connections[cave1].add(cave2)
        if not cave1 == "start" and not cave2 == "end":
            connections[cave2].add(cave1)
    return connections



def is_small_cave(cave):
    return cave.islower()


def find_paths(src, connections, visited=list(), paths=list()):
    connections = deepcopy(connections)
    visited = deepcopy(visited)
    paths = deepcopy(paths)

    if src == "end":
        visited.append(src)
        paths.append(visited)
        return paths
    elif not connections[src]:
        return paths
    elif is_small_cave(src):
        visited.append(src)

        for dst in connections[src]:
            new_connections = deepcopy(connections)

            # if I just visited a small cave, I can't go back to it,
            # therefore, I remove it as a candidate from the various connections            
            for k in connections[src]:
                new_connections[k] = new_connections[k].difference({src})
            
            paths = find_paths(dst, new_connections, visited, paths)
    else:
        visited.append(src)

        for dst in connections[src]:
            paths = find_paths(dst, connections, visited, paths)
    return paths

