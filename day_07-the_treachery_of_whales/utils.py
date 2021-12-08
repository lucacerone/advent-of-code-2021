import numpy as np

def import_positions(path):
    with open(path,"r") as fh:
        positions = fh.readline().rstrip().split(",")
    positions = np.array([int(p) for p in positions])
    return positions

def fuel_consumed(pos, positions):
    return np.abs(positions - pos).sum()

def fuel_consumed_incremental(pos, positions):
    deltas = np.abs(positions - pos)
    consumptions = np.multiply(deltas, deltas+1) / 2
    return consumptions.sum()
