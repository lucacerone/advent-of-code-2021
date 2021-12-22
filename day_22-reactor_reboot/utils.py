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
        line = line.rstrip()

        match = re.search(INPUT_REGEX, line)
        if match:
            d = match.groupdict()
            for k in ["min_x", "max_x", "min_y", "max_y", "min_z", "max_z"]:
                d[k] = int(d[k])
            data.append(d)
    return data


def in_limits(d, min_coord=-50, max_coord=50):
    return (
        d["min_x"] >= min_coord
        and d["max_x"] <= max_coord
        and d["min_y"] >= min_coord
        and d["max_y"] <= max_coord
        and d["min_z"] >= min_coord
        and d["max_z"] <= max_coord
    )


class Cuboid:
    def __init__(
        self, min_x: int, max_x: int, min_y: int, max_y: int, min_z: int, max_z: int
    ) -> None:
        self._min_x, self._max_x = min_x, max_x
        self._min_y, self._max_y = min_y, max_y
        self._min_z, self._max_z = min_z, max_z

        self._cubes = (
            (max_x - min_x +1)*
            (max_y - min_y +1)*
            (max_z - min_z +1)
        )
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._min_x}, {self._max_x}, {self._min_y}, {self._max_y}, {self._min_z}, {self._max_z})"
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} made of {self._cubes} cube{'s' if self._cubes > 1 else ''}"
    
    def overlaps_with(self, other:"Cuboid") -> bool:
        return False

