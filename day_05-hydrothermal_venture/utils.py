import fileinput
import numpy as np

def parse_line(line):
    line = line.rstrip()
    components = line.split(" -> ")
    origin = tuple(int(x) for x in components[0].split(","))
    destination = tuple(int(x) for x in components[1].split(","))
    return origin, destination

def is_horizontal_line(origin, destination):
    return origin[0] == destination[0]

def is_vertical_line(origin, destination):
    return origin[1] == destination[1]

def is_diagonal_line(origin, destination):
    delta_x = abs(origin[0] - destination[0])
    delta_y = abs(origin[1] - destination[1])
    return delta_x == delta_y

def is_straight_line(origin, destination):
    return is_horizontal_line(origin, destination) or is_vertical_line(origin, destination)

def is_straight_or_diagonal_line(origin, destination):
    return is_straight_line(origin, destination) or is_diagonal_line(origin, destination)

def import_hydrothermal_lines(path, filter_fun=is_straight_line):
    hydrothermal_lines = []
    for line in fileinput.input(path):
        origin, destination = parse_line(line)
        if filter_fun(origin, destination):
            hydrothermal_lines.append([origin, destination])
    return hydrothermal_lines

def get_x_size(hydrothermal_lines):
    return max([max(origin[0],destination[0]) for origin, destination in hydrothermal_lines]) + 1

def get_y_size(hydrothermal_lines):
    return max([max(origin[1],destination[1]) for origin, destination in hydrothermal_lines]) + 1

def make_empty_hydrothermal_map(hydrothermal_lines):
    x_size = get_x_size(hydrothermal_lines)
    y_size = get_y_size(hydrothermal_lines)
    return np.zeros(shape=(x_size, y_size))

def _get_min_y_max_y(origin, destination):
    min_y = min(origin[1], destination[1])
    max_y = max(origin[1], destination[1]) +1
    return min_y, max_y

def add_horizontal_line(hydrothermal_map, origin, destination):
    min_y, max_y = _get_min_y_max_y(origin, destination)    
    x = origin[0]
    hydrothermal_map[x,min_y:max_y] += 1

def _get_min_x_max_x(origin, destination):
    min_x = min(origin[0], destination[0])
    max_x = max(origin[0], destination[0]) +1
    return min_x, max_x

def add_vertical_line(hydrothermal_map, origin, destination):
    min_x, max_x = _get_min_x_max_x(origin, destination)
    y = origin[1]
    hydrothermal_map[min_x:max_x, y] += 1

def add_diagonal_line(hydrothermal_map, origin, destination):
    delta_x = destination[0] - origin[0]
    delta_y = destination[1] - origin[1]

    for offset in range(abs(delta_x)+1):
        x = origin[0] + np.sign(delta_x)*offset
        y = origin[1] + np.sign(delta_y)*offset
        hydrothermal_map[x,y] += 1
  
def add_line(hydrothermal_map, origin, destination):
    if is_horizontal_line(origin, destination):
        add_horizontal_line(hydrothermal_map, origin, destination)
    elif is_vertical_line(origin, destination):
        add_vertical_line(hydrothermal_map, origin, destination)
    elif is_diagonal_line(origin, destination):
        add_diagonal_line(hydrothermal_map, origin, destination)
    else:
        raise ValueError(f"{origin} -> {destination} is not a straight line")

def populate_hydrothermal_map(hydrothermal_map, hydrothermal_lines):
    for origin, destination in hydrothermal_lines:
        add_line(hydrothermal_map, origin, destination)
