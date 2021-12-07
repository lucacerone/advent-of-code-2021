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
