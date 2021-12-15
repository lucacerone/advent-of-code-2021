import fileinput
import numpy as np

def import_data(path):
    matrix = []
    for line in fileinput.input(path):
        matrix.append([int(v) for v in line.rstrip()])
    return np.array(matrix)

def get_adjacent_coordinates(matrix, i,j):
        max_i = matrix.shape[0] -1
        max_j = matrix.shape[1] -1
        
        if i < 0 or i > max_i or j < 0 or j > max_j:
            raise ValueError(f"Incompatible coordinates {(i,j)}")

        adjacent = []
        if i >= 1: adjacent.append((i-1,j))
        if j >= 1: adjacent.append((i,j-1))
        if j < max_j: adjacent.append((i,j+1))
        if i < max_i: adjacent.append((i+1,j))

        return adjacent

def get_adjacent_values(matrix, i,j):
    return [matrix[pos] for pos in get_adjacent_coordinates(matrix,i,j)]


def find_unvisited_node_with_smallest_tentative_distance(unvisited, distance):
    current_min_node = None
    for node in unvisited:
        if current_min_node is None:
            current_min_node = node
        elif distance[node] < distance[current_min_node]:
                current_min_node = node
        else:
            continue
    return current_min_node

