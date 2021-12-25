import utils as u

from heapq import heappush, heappop
from copy import deepcopy

data = """\
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

STEP_COSTS = {
  "A": 1,
  "B": 10,
  "C": 100,
  "D": 1000
}

class Hallway
