from copy import deepcopy

STEP_COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

Empty = "."


class Hallway:
    def __init__(self, state) -> None:
        self._state = state

    def insert(self, element, pos):
        if element == Empty:
            raise ValueError(f"Can't insert an empty space.")
        if self._state[pos] != Empty:
            raise ValueError(f"Can't insert '{element}' in position {pos}.")

        new_state = self._state[:pos] + (element,) + self._state[pos+1:]
        return Hallway(new_state)

    def remove(self, pos):
        if self._state[pos] == Empty:
            raise ValueError(f"Position {pos} is empty.")

        new_state = self._state[:pos] + (Empty,) + self._state[pos + 1 :]
        return Hallway(new_state)

    def _can_move_from_to(self, start, end):
        path = self._state

        # can't move to the same position:
        if start == end:
            return False

        # can't move if the destination is occupied:
        if path[end] != Empty:
            return False

        if start < end:
            start_idx = start + 1
            end_idx = end
        elif start > end:
            start_idx = end + 1
            end_idx = start

        # check that all the point between start and end (ends not included) are empty
        return all(map(lambda x: x == ".", path[start_idx:end_idx]))

    def __hash__(self) -> int:
        return hash(self._state)

    def __eq__(self, other) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self._state == other._state
    
    def __lt__(self, other) -> bool:
        return self._state < other._state

    def __repr__(self) -> str:
        return f"{''.join(self._state)}"


class Room:
    def __init__(self, state, guest_type, pos) -> None:
        self._state = state
        self._guest_type = guest_type
        self._position = pos

    def insert(self, element, pos):
        if element == Empty:
            raise ValueError(f"Can't insert an empty space.")
        if self._state[pos] != Empty:
            raise ValueError(f"Can't insert '{element}' in position {pos}.")

        new_state = self._state[:pos] + (element,) + self._state[pos + 1 :]
        return Room(new_state, self._guest_type, self._position)

    def remove(self, pos):
        if self._state[pos] == Empty:
            raise ValueError(f"Position {pos} is empty.")

        new_state = self._state[:pos] + (Empty,) + self._state[pos + 1 :]
        return Room(new_state, self._guest_type, self._position)

    def _can_exit_from(self, pos: int) -> bool:
        path = self._state
        if path[pos] == Empty:
            return False  # can't move an empty space
        
        # if the path on the hallway is blocked, return False
        if any(map(lambda x: x != Empty, path[:pos])):
            return False
        
        # if the item is not the same as the room guest type it can go exit the roome:
        if path[pos] != self._guest_type:
            return True
        else:
            # however, if the element is the same of the room guest type,
            # it can leave the room if it's locking the way to other types,
            # otherwise it can't go out
            return any(map(lambda x: x != Empty and x != self._guest_type, path[pos+1:]))


    def _can_enter_to(self, val, pos):
        path = self._state

        # can't let in a guest that hasn't the right type
        if val != self._guest_type:
            return False

        # can't enter if any of the other guests currently in the room is not of the right type
        if any(map(lambda x: x != Empty and x != self._guest_type, path)):
            return False

        # can't enter to a position that is already occupied
        if path[pos] != Empty:
            return False

        # can't enter if there is a non empty space in between
        if any(map(lambda x: x != Empty, path[:pos])):
            return False
        
        # can't enter if there are empty spaces past the destination position
        if any(map(lambda x: x==Empty, path[pos+1:])):
            return False

        return True

    def __hash__(self) -> int:
        return hash((self._state, self._guest_type, self._position))

    def __eq__(self, other:"Room") -> int:
        if not isinstance(other, type(self)):
            return False
        return (
            self._state == other._state
            and self._guest_type == other._guest_type
            and self._position == other._position
        )
    
    def __lt__(self, other):
        return (self._state, self._guest_type, self._position) < (other._state, other._guest_type, other._position)

    def __repr__(self) -> str:
        return f"({self._guest_type}, {self._state}, {self._position}"


class Configuration:
    def __init__(self, hallway, rooms) -> None:
        self._hallway = hallway
        self._rooms = rooms
        self._forbidden_positions = set(r._position for r in self._rooms.values())

    def __hash__(self) -> int:
        return hash((self._hallway, tuple(self._rooms.items())))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        return (
            hash(self)
            and hash(other)
            and self._hallway == other._hallway
            and self._rooms == other._rooms
        )
    
    def next_configurations(self):
        hallway = self._hallway
        for hallway_pos, hallway_val in enumerate(hallway._state):
            if hallway_pos in self._forbidden_positions: continue
            for room_name, room in self._rooms.items():
                for pos_in_room, room_guest in enumerate(room._state):
                    if room._can_exit_from(pos_in_room) and hallway._can_move_from_to(room._position, hallway_pos):
                        new_hallway = hallway.insert(room_guest, hallway_pos)
                        new_room = room.remove(pos_in_room)
                        new_rooms = deepcopy(self._rooms)
                        new_rooms[room_name] = new_room
                        new_configuration = Configuration(new_hallway, new_rooms)
                        
                        n_steps = pos_in_room+1 + abs(hallway_pos-room._position)
                        transition_cost = STEP_COSTS[room_guest]*n_steps
                        yield transition_cost, new_configuration
                    
                    if room._can_enter_to(hallway_val, pos_in_room) and hallway._can_move_from_to(hallway_pos, room._position):
                        new_hallway = hallway.remove(hallway_pos)
                        new_room = room.insert(hallway_val, pos_in_room)
                        new_rooms = deepcopy(self._rooms)
                        new_rooms[room_name] = new_room
                        new_configuration = Configuration(new_hallway, new_rooms)
                        n_steps = pos_in_room+1 + abs(hallway_pos-room._position)
                        transition_cost = STEP_COSTS[hallway_val]*n_steps
                        yield transition_cost, new_configuration


    def __lt__(self, other):
        return (self._hallway, tuple(self._rooms.items())) < (
            other._hallway,
            tuple(other._rooms.items()),
        )

    def __repr__(self) -> str:
        return f"|hallway: {repr(self._hallway)}, rooms: {repr(self._rooms)}|"
