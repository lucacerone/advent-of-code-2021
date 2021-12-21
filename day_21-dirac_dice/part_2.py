from utils import PlayerState, countVictories, countVictories_v2

# Example positions:
#p1 = PlayerState(position=4, score=0)
#p2 = PlayerState(position=8, score=0)

# Input positions
p1 = PlayerState(position=5, score=0)
p2 = PlayerState(position=9, score=0)

victories = countVictories(p1,p2, current_player=1)

solution = max(victories)
print(f"Solution V1: {solution}")

victories_v2 = countVictories_v2(p1,p2, current_player=1)
solution_v2 = max(victories_v2)
print(f"Solution V2: {solution_v2}")
