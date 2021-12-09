import utils as u

heights = u.import_data("./data/input")

n_rows, n_columns = heights.shape

low_points = []
for i in range(n_rows):
    for j in range(n_columns):
        current = heights[i,j]
        adjacent = u.get_adjacent_points(heights, i, j)
        if u.is_low_point(current, adjacent):
            low_points.append((i,j))

basins = [u.find_basin_non_recursive(lp, heights) for lp in low_points]
basins_sizes = list(map(lambda b: len(b), basins))
basins_sizes.sort()

value = 1
for bs in basins_sizes[-3:]:
    value *= bs

print(f"The product of the three largest basins is {value}")
