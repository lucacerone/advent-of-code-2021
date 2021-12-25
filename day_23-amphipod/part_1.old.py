import io
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

hallway = (".",) * 11

rooms = (
    ("A", (".", "A"), 2),
    ("B", (".", "A"), 4),
    ("C", ("B", "C"), 6),
    ("D", ("D", "A"), 8)
)

final_state = (("A","A")+(".",)*9, (
    ("A", (".", "."), 2),
    ("B", (".", "."), 4),
    ("C", ("C", "C"), 6),
    ("D", ("D", "D"), 8)
))

forbidden = set([r[2] for r in rooms])

visited = set()

initial_state = (hallway, rooms)
initial_cost = 0
costs_states = {initial_state: initial_cost}

queue = [(initial_cost, initial_state)]


i=0
while queue:
    if final_state in visited:
      print("final state in visited")
      break
    current_cost, current_state = heappop(queue)

    if current_state in visited:
        continue

    current_hallway, current_rooms = current_state
    
    # this part checks the possible movements from rooms to the hallway
    for room_idx, (src_room, room_guests, ac) in enumerate(current_rooms):
        for ar, amphipod in enumerate(room_guests):
          if amphipod == ".": continue
          if any(map(lambda x: x != ".", room_guests[:ar])): continue
          for hc, hallway_guest in enumerate(current_hallway):
              if hc in forbidden: continue  # if the space is forbidden, you can't move an amphipod there
              if hallway_guest != ".": continue # if the space is occupied you can't move an amphipod there

              # check whether the path is blocked by another amphipod, if it is continue
              min_c = min(ac,hc)
              max_c = max(ac,hc)
              if any(map(lambda x: x != ".", current_hallway[min_c:max_c])): continue 

              new_hallway = current_hallway[:hc] + (amphipod,) + current_hallway[hc+1:]
              
              new_room_guests = list(room_guests)
              new_room_guests[ar] = "."
              new_room_guests = tuple(new_room_guests)

              new_rooms = list(current_rooms)
              new_rooms[room_idx] = (src_room, new_room_guests, ac)
              new_rooms = tuple(new_rooms)

              new_state = (new_hallway, new_rooms)

              n_steps = abs(hc-ac)+ar+1
              transition_cost = n_steps*STEP_COSTS[amphipod]
              new_cost = current_cost + transition_cost

              if new_state not in costs_states or new_cost < costs_states[new_state]:
                costs_states[new_state] = new_cost
                heappush(queue, (new_cost, new_state))
    
    # this part checks the possible movements from the hallway to the rooms:
    for ac, amphipod in enumerate(current_hallway):
      if amphipod=="." or ac in forbidden: continue # if the location is empty, nothing to do      
      for room_idx, (dst_room, room_guests, rc) in enumerate(current_rooms):
        if amphipod != dst_room: continue # if it's not the right room, continue
        
        # check whether the path is blocked by another amphipod, if it is continue
        min_c = min(ac,rc)
        max_c = max(ac,rc)
        if any(map(lambda x: x != ".", current_hallway[min_c:max_c])): continue
        
        """
        if not all(map(lambda x: x=="." or x==amphipod, room_guests)): continue # if in the room there's any amphipod different from the one you want to move, continue
        for rr, _ in enumerate(room_guests):
          if not all(map(lambda x: x==".", room_guests[:rr+1])): continue # check that the path to the position in the room is free, otherwise continue

          if any(map(lambda x: x==".", room_guests[rr+1:])): continue

          new_hallway = current_hallway[:ac] + (".",) + current_hallway[ac+1:]
          
          new_room_guests = list(room_guests)
          new_room_guests[rr] = amphipod
          new_room_guests = tuple(new_room_guests)

          new_rooms = list(current_rooms)
          new_rooms[room_idx] = (dst_room, new_room_guests, rc)
          new_rooms = tuple(new_rooms)

          new_state = (new_hallway, new_rooms)

          n_steps = abs(rc-ac)+rr+1
          transition_cost = n_steps*STEP_COSTS[amphipod]
          new_cost = current_cost + transition_cost

          if new_state == final_state:
            print("final state found, cost:", new_cost)
            print(current_cost, current_state)
            print(new_cost, new_state)

          if new_state not in costs_states or new_cost < costs_states[new_state]:
            costs_states[new_state] = new_cost
            heappush(queue, (new_cost, new_state))
        """

    visited.add(current_state)
    i+=1

