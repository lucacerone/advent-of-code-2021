import re

INPUT_REGEX = re.compile(
    "^(?P<action>on|off) "
    "x=(?P<min_x>[-]{,1}\d+)\.{2}(?P<max_x>[-]{,1}\d+),"
    "y=(?P<min_y>[-]{,1}\d+)\.{2}(?P<max_y>[-]{,1}\d+),"
    "z=(?P<min_z>[-]{,1}\d+)\.{2}(?P<max_z>[-]{,1}\d+)\s*$"
)

def import_data(fh):
    data = []
    for line in fh:
        line=line.rstrip()

        match = re.search(INPUT_REGEX, line)
        if match:
            d = match.groupdict()
            for k in ['min_x', 'max_x', 'min_y', 'max_y', 'min_z', 'max_z']:
                d[k] = int(d[k])
            data.append(d)
    return data

def in_limits(d, min_coord=-50, max_coord=50):
    return (
        d['min_x'] >= min_coord and d['max_x'] <= max_coord and
        d['min_y'] >= min_coord and d['max_y'] <= max_coord and
        d['min_z'] >= min_coord and d['max_z'] <= max_coord
    )
