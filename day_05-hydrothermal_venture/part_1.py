from utils import (
    import_hydrothermal_lines,
    is_straight_line,
    make_empty_hydrothermal_map,
    populate_hydrothermal_map
)


hydrothermal_lines = import_hydrothermal_lines("./data/input", filter_fun=is_straight_line)
hydrothermal_map = make_empty_hydrothermal_map(hydrothermal_lines)
populate_hydrothermal_map(hydrothermal_map, hydrothermal_lines)

n_dangerous_points =  hydrothermal_map[hydrothermal_map >= 2.].shape[0]
print(f"There are {n_dangerous_points} points in the map")
