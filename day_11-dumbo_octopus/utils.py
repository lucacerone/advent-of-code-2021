import fileinput
import numpy as np


def import_data(path):
    data = []
    for line in fileinput.input(path):
        data.append([int(d) for d in line.rstrip()])
    return np.array(data)

def get_neighbors_positions(data, pos):
    x,y = pos
    n_rows, n_cols = data.shape
    positions = []
    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if i >= 0 and i <= (n_rows -1) and j >= 0 and j <= (n_cols - 1) and not (i,j) == pos:
                positions.append((i,j))
    return positions

def get_neighbors_values(data, pos):
    neighbors_positions = get_neighbors_positions(data, pos)
    values = []
    for i,j in neighbors_positions:
        values.append(data[i,j])
    return np.array(values, dtype=data.dtype)

