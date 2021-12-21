from typing import Type


class SnailfishNumber:
    def __init__(self, left, right) -> None:
        self._left = left
        self._right = right
        self.reduce()

    @classmethod
    def from_list(cls, l) -> "SnailfishNumber":
        assert len(l) == 2
        return cls(l[0],l[1])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._left}, {self._right})"
    
    def __str__(self) -> str:
        return f"[{self._left}, {self._right}]"

    def __add__(self, other: "SnailfishNumber") -> "SnailfishNumber":
        return SnailfishNumber([self._left, self._right], [other._left, other._right])

    def explode(self):
       if isinstance(self._left, int):
           return self
        
        
    
    def split(self):
        pass
    
    def reduce(self):
        pass
