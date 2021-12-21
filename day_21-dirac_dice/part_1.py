from utils import deterministic_die, update_player_state, PlayerState

rolls_per_turn = 3
die = deterministic_die(rolls = rolls_per_turn)


# Example positions:
#p1 = PlayerState(position=4, score=0)
#p2 = PlayerState(position=8, score=0)

# Input positions
p1 = PlayerState(position=5, score=0)
p2 = PlayerState(position=9, score=0)

verbose = False

n_rolls=0
while True:
    rolled = next(die)
    n_rolls += rolls_per_turn
    p1 = update_player_state(p1, rolled)
    if verbose: print("[Player 1] rolled:", rolled, p1)
    if p1.score >= 1000:
        break
    
    rolled = next(die)
    n_rolls += rolls_per_turn
    p2 = update_player_state(p2, rolled)
    if p2.score >= 1000:
        break
    if verbose: print("[Player 2] rolled:", rolled, p2)


loser = p1 if p1.score < p2.score else p2
solution = n_rolls * loser.score
print(f"Solution: {solution}")
