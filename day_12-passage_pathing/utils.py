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


def count_paths(src, connections, counter=0):
    if src == "end":
        return counter + 1
    elif not connections[src]:
        return counter
    elif is_small_cave(src):
        for dst in connections[src]:
            new_connections = deepcopy(connections)

            # if I just visited a small cave, I can't go back to it,
            # therefore, I remove it as a candidate from the various connections            
            for k in connections[src]:
                new_connections[k] = new_connections[k].difference({src})
            counter = count_paths(dst, new_connections, counter)
    else:
        for dst in connections[src]:
            counter = count_paths(dst, connections, counter)
    return counter


def count_paths2(src, connections, visited=list(), counter=0):
    visited = deepcopy(visited)
    visited.append(src)
    
    if src == "end":
        return counter + 1
    elif not connections[src]:
        return counter
    elif is_small_cave(src):
        for dst in connections[src]:
            new_connections = deepcopy(connections)
        
            for k in connections[src]:
                new_connections[k] = new_connections[k].difference({src})
            counter = count_paths(dst, new_connections, visited, counter)
    else:
        for dst in connections[src]:
            counter = count_paths(dst, connections, visited, counter)
    return counter

