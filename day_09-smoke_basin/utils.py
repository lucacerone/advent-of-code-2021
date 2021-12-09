import fileinput
import numpy as np

def import_data(path):
    matrix = []
    for line in fileinput.input(path):
        matrix.append([int(v) for v in line.rstrip()])
    return np.array(matrix)

def get_adjacent_points(heights, i, j):
        n_rows = heights.shape[0]
        n_columns = heights.shape[1]

        adjacent = []
        
        if i>=1:
            adjacent.append(heights[i-1,j])
        
        if j>= 1:
            adjacent.append(heights[i, j-1])
        
        if j < n_columns -1:
            adjacent.append(heights[i, j+1])
        
        if i < n_rows -1:
            adjacent.append(heights[i+1,j])
        
        return np.array(adjacent)

def get_adjacent_coordinates(heights, coords):
        n_rows = heights.shape[0]
        n_columns = heights.shape[1]

        adjacent = []

        i, j = coords
        
        if i>=1:
            adjacent.append((i-1,j))
        
        if j>= 1:
            adjacent.append((i,j-1))
        
        if j < n_columns -1:
            adjacent.append((i,j+1))
        
        if i < n_rows -1:
            adjacent.append((i+1,j))
        
        return adjacent

def is_low_point(current, adjacent):
    return np.all(current < adjacent)


def find_basin(current_coords, heights, basin = None):
    if basin is None:
        basin = set()
    basin.add(current_coords)

    adjacent_coords = get_adjacent_coordinates(heights, current_coords)
    
    current_value = heights[current_coords]
    for acoord in adjacent_coords:
        adj_value = heights[acoord]
        if acoord not in basin and adj_value != 9 and current_value < adj_value:
            basin = find_basin(acoord, heights, basin)
        else:
            continue
    return basin


def find_basin_non_recursive(low_point, heights):
    basin = set()
    to_visit = [low_point]

    while to_visit:
        current_coords = to_visit.pop(0)
        current_val = heights[current_coords]
        basin.add(current_coords)
        adjacent_coords = get_adjacent_coordinates(heights, current_coords)
        for adj_coords in adjacent_coords:
            adj_val = heights[adj_coords]
            if adj_coords not in basin and adj_val != 9 and current_val < adj_val:
                to_visit.append(adj_coords)
    
    return basin
