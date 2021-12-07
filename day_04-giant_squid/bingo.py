import numpy as np


class BingoBoard:
    def __init__(self, board: np.array) -> None:
        self._board = board
        self._rows = self._board.shape[0]
        self._columns = self._board.shape[1]
        self._marked = np.zeros_like(self._board)
    
    def unmarked_sum(self):
        return self._board[self._marked==0].sum()

    def mark_list(self, number_list):
        for number in number_list:
            self.mark(number)

    def mark(self, number):
        if number in self:
            row, col = self._get_position(number)
            self._marked[row, col] = 1
    
    def is_winning(self):
        return self._has_full_horizontal() or self._has_full_vertical()

    def _has_full_horizontal(self):
        return np.any(self._marked.sum(axis=1) == self._columns)

    def _has_full_vertical(self):
        return np.any(self._marked.sum(axis=0) == self._rows)

    def _get_position(self, number):
        pos_arrays = np.where(self._board == number)
        row = pos_arrays[0][0]
        col = pos_arrays[1][0]
        return row, col

    def __contains__(self, number):
        return number in self._board

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self._board)})"

    def __str__(self) -> str:
        return str(self._board)
