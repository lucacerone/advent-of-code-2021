from io import FileIO
from typing import TextIO

import numpy as np

from bingo import BingoBoard

def import_drawn_number(path):
    with open(path, "r") as fh:
        values = fh.readline().rstrip()
    return list(map(int, values.split(",")))


def _skip_header(fh):
    _ = fh.readline()  # skip drawn numbers
    _ = fh.readline()
    return None


def import_boards(path, rows=5, columns=5):
    boards = []
    with open(path, "r") as fh:
        _skip_header(fh)

        while True:
            boards.append(_import_board(fh, rows=rows, columns=columns))
            _ = fh.readline() # skip empty line
            if not _:
                break
        return boards


def _import_board(fh: TextIO, rows=5, columns=5) -> BingoBoard:
    board = []
    for i in range(rows):
        line = fh.readline().rstrip().split(" ")
        row = [int(n) for n in line if n]
        board.append(row)
    board = np.array(board)
    assert board.shape[0] == rows
    assert board.shape[1] == columns
    return BingoBoard(board)
