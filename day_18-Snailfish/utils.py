from typing import Type


class SnailfishNumber:
    def __init__(self, left, right) -> None:
        self._left = left
        self._right = right
        self.reduce()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._left}, {self._right})"
    
    def __str__(self) -> str:
        return f"[{self._left}, {self._right}]"

    def __add__(self, other: "SnailfishNumber") -> "SnailfishNumber":
        return SnailfishNumber([self._left, self._right], [other._left, other._right])

    def explode(self):
        try:
            for i, number in enumerate(self._left):
                if i < 4:
                    continue
                else:
                    print("To explode:", number)
                    break
        except TypeError:
            print("nothing to be done")
    
    def split():
        pass
    
    def reduce(self):
        pass
