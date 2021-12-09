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
            basin.update(find_basin(acoord, heights, basin))
        else:
            continue
    return basin
