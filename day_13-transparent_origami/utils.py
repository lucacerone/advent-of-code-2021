import numpy as np
from functools import reduce

def import_instructions(path):
    with open(path,"r") as fh:
        diagram, folds = _read_instructions(fh)
    matrix = _diagram_to_matrix(diagram)
    return matrix, folds

def _read_instructions(fh):
    diagram = []
    for line in fh:
        if line == "\n":
            break

        line = line.rstrip()
        x,y = line.split(",")
        diagram.append([int(x), int(y)])
    
    folds = []
    for line in fh:
        line = line.rstrip()
        instruction = line.split(" ")
        where, idx = instruction[-1].split("=")
        folds.append((where, int(idx)))
    
    return diagram, folds

def _diagram_to_matrix(diagram):
    max_x = max([x for x,y in diagram])+1
    max_y = max([y for x,y in diagram])+1

    matrix = np.zeros(shape=(max_y, max_x), dtype=int)
    for j,i in diagram:
        matrix[i,j] = 1
    return matrix

def fold_along_y(diagram,y):
    top = diagram[:y,:]
    
    bottom = diagram[(y+1):, :]
    # we flip the bottom part upside down to do the fold
    bottom = bottom[::-1,:]
    
    if top.shape[0] < bottom.shape[0]:
        pads = np.zeros((bottom.shape[0] - top.shape[0], top.shape[1]), dtype=int)
        top = np.concatenate((pads, top), axis=0)
    elif top.shape[0] > bottom.shape[0]:
        pads = np.zeros((top.shape[0] - bottom.shape[0], bottom.shape[1]), dtype=int)
        bottom = np.concatenate((pads, bottom), axis=0)
    else:
        # matrices have the same number of rows, no pad needed
        pass
    
    folded = np.bitwise_or(top, bottom)
    return folded

def fold_along_x(diagram,x):
    left = diagram[:,:x]
    
    right = diagram[:, (x+1):]
    # we flip the bottom part left to right to do the fold
    right = right[:,::-1]
    
    if left.shape[1] < right.shape[1]:
        pads = np.zeros((left.shape[0], right.shape[1] - left.shape[1]), dtype=int)
        left = np.concatenate((pads, left), axis=1)
    elif left.shape[1] > right.shape[1]:
        pads = np.zeros((right.shape[0], left.shape[1] - right.shape[1]), dtype=int)
        right = np.concatenate((pads, right), axis=1)
    else:
        # matrices have the same number of rows, no pad needed
        pass
    
    folded = np.bitwise_or(left, right)
    return folded
    
    
def apply_instruction(instruction, matrix):
    inst_type , value = instruction

    if inst_type == "y":
        return fold_along_y(matrix, value)
    elif inst_type == "x":
        return fold_along_x(matrix, value)
    else:
        raise ValueError(f"Unknown instruction '{inst_type}'")


def diagram_to_string(diagram):
    X = [[u"\u2588" if v else " " for v in y] for y in diagram]
    return reduce(lambda x,y: x+"\n"+y, map(lambda x: "".join(x), X))

def print_diagram(diagram):
    print(diagram_to_string(diagram))
