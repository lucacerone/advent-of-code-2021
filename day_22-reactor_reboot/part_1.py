import utils as u

from io import StringIO

with open("./data/input") as fh:
    data = u.import_data(fh)


points = dict()
for instruction in data:
    if not u.in_limits(instruction):
        continue

    if instruction["action"] == "on":
        value = 1
    elif instruction["action"] == "off":
        value = 0
    else:
        raise ValueError("wrong instruction")

    for x in range(instruction['min_x'], instruction['max_x']+1):
        for y in range(instruction['min_y'], instruction['max_y']+1):
            for z in range(instruction['min_z'], instruction['max_z']+1):
                points[(x,y,z)] = value

n_points = sum(points.values())

print(f"N. Lights: {n_points}")
