import numpy as np

from utils import (
    import_positions, 
    fuel_consumed_incremental
)

positions = import_positions("./data/input")

min_pos = positions.min()
max_pos = positions.max()

fuel_consumption = np.array([fuel_consumed_incremental(i, positions) for i in range(min_pos, max_pos)])

print(f"The minimum amount of fuel consumed is {fuel_consumption.min()}")
