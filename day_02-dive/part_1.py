import sys
import fileinput


class Position():
    def __init__(self, horizontal=0, depth=0):
        self._horizontal = horizontal
        self._depth = depth
    
    @property
    def coordinates(self):
        return {"horizontal": self._horizontal, "depth": self._depth}
    
    def __repr__(self):
        return f"{self.__class__.__name__}(horizontal={self._horizontal}, depth={self._depth})"
    
    def __str__(self):
        return str(self.coordinates)

    def forward(self, x):
        self._horizontal += x
        return self

    def up(self, x):
        self._depth -= x
        return self

    def down(self, x):
        self._depth += x
        return self

    def update(self, action, value):
        return getattr(self, action)(value)

def parse_instruction(instruction):
    action, value = instruction.rstrip().split(" ")
    return action, int(value)

def main():
    instructions_file = "./data/input"
    current = Position()

    for instruction in fileinput.input(instructions_file):
        action, value = parse_instruction(instruction)
        current.update(action, value)
    
    coordinates = current.coordinates
    print(f"Horizontal x Depth = {coordinates['horizontal']} x {coordinates['depth']} = {coordinates['horizontal'] * coordinates['depth']}")

    return 0

if __name__ == "__main__":
    status = main()
    sys.exit(status)
