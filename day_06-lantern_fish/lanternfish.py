import numpy as np

NEW_LANTERFISH_TIMER = 8
RESET_LANTERFISH_TIMER = 6

class Lanternfish:
    def __init__(self, current) -> None:
        self._timer = current
    
    def reset_timer(self):
        self._timer = RESET_LANTERFISH_TIMER
    
    def age(self):
        self._timer -= 1

        if self._timer < 0:
            self.reset_timer()
            return Lanternfish(NEW_LANTERFISH_TIMER)
    
    def __repr__(self) -> str:
        return f"{self._timer}"


class LanterfishSchool:
    def __init__(self, initial_states) -> None:
        self._school = [Lanternfish(timer) for timer in initial_states]
    
    def age(self):
        new_lanternfishes = []
        for lf in self._school:
            newborn = lf.age()
            if newborn:
                new_lanternfishes.append(newborn)
        self._school.extend(new_lanternfishes)
        
        return self
    
    def size(self):
        return len(self)
    
    def __len__(self):
        return len(self._school)
      
    def __repr__(self) -> str:
        return repr(self._school)


class LanterfishSchoolAggregated:
    def __init__(self, initial_states) -> None:
        self._state = np.zeros(9, dtype=int)
        for state in initial_states:
            self._state[state] +=1
    
        self._transition_matrix = np.array([
            [0,1,0,0,0,0,0,0,0], # 0
            [0,0,1,0,0,0,0,0,0], # 1
            [0,0,0,1,0,0,0,0,0], # 2
            [0,0,0,0,1,0,0,0,0], # 3
            [0,0,0,0,0,1,0,0,0], # 4
            [0,0,0,0,0,0,1,0,0], # 5
            [1,0,0,0,0,0,0,1,0], # 6
            [0,0,0,0,0,0,0,0,1], # 7
            [1,0,0,0,0,0,0,0,0]  # 8
        ], dtype=int)
    
    def age(self):
        self._state = np.matmul(self._transition_matrix, self._state)

    def size(self):
        return self._state.sum()
    
    def __str__(self) -> str:
        return str(self._state)
    
    def __repr__(self) -> str:
        return str(self)
