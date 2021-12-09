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

def is_low_point(current, adjacent):
    return np.all(current < adjacent)

def find_basin(i,j)
