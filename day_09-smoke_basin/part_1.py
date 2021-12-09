import numpy as np
import utils as u

heights = u.import_data("./data/input")

n_rows, n_columns = heights.shape

low_points = np.array([])
for i in range(n_rows):
    for j in range(n_columns):
        current = heights[i,j]
        adjacent = u.get_adjacent_points(heights, i, j)
        if u.is_low_point(current, adjacent):
            low_points = np.append(low_points, current)

risk_levels = low_points +1
print("The sum of the risk levels is", risk_levels.sum())
