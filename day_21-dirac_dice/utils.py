import itertools

from functools import cache
from collections import namedtuple

PlayerState = namedtuple("PlayerState",["position", "score"])

def deterministic_die(rolls=3):
    values = list(range(1,101))
    i=0
    while True:
        indices = [idx % 100 for idx in range(i, i+rolls)]
        rolled = tuple(values[idx] for idx in indices)
        i = (i+rolls) % 100
        yield rolled


def update_player_state_from_rolls(player, rolled):
    dice_sum = sum(rolled)
    return update_player_state_from_dice_sum(player, dice_sum)



def update_player_state_from_dice_sum(player, dice_sum):
    new_position = (player.position + dice_sum) % 10
    new_position = new_position if new_position else 10
    
    new_score = player.score + new_position

    return PlayerState(position=new_position, score=new_score)


### CODE FOR PART 2

POSSIBLE_ROLLS = list(itertools.product(range(1,4), range(1,4), range(1,4)))

POSSIBLE_SUMS = {}
for s in map(sum, POSSIBLE_ROLLS):
    POSSIBLE_SUMS[s] = POSSIBLE_SUMS.get(s,0) + 1

@cache
def update_game_state_from_dice_sum(p1, p2, current_player, dice_sum):
    if current_player == 1:
        p1 = update_player_state_from_dice_sum(p1,dice_sum)
        next_player = 2
    elif current_player == 2:
        p2 = update_player_state_from_dice_sum(p2, dice_sum)
        next_player = 1
    else:
        raise ValueError(f"Unknown current player {current_player}")
    
    return p1, p2, next_player

@cache
def update_game_state_from_rolls(p1, p2, current_player, rolls):
    dice_sum = sum(rolls)
    return update_game_state_from_dice_sum(p1, p2, current_player, dice_sum)


@cache
def countVictories(p1, p2, current_player, SCORE_TO_WIN=21):
    if p1.score >= SCORE_TO_WIN:
        return (1,0)
    
    if p2.score >= SCORE_TO_WIN:
        return (0,1)

    v1, v2 = 0, 0
    for rolls in POSSIBLE_ROLLS:
        new_p1, new_p2, new_current_player = update_game_state_from_rolls(p1, p2, current_player, rolls)
        a1, a2 = countVictories(new_p1, new_p2, new_current_player)
        v1+=a1
        v2+=a2
    return v1, v2    


@cache
def countVictories_v2(p1, p2, current_player, SCORE_TO_WIN=1):
    if p1.score >= SCORE_TO_WIN:
        return (1, 0)
    
    if p2.score >= SCORE_TO_WIN:
        return (0,1)
    
    v1, v2 = 0,0
    for dice_sum, n_universes in POSSIBLE_SUMS.items():
        new_p1, new_p2, new_current_player = update_game_state_from_dice_sum(p1, p2, current_player, dice_sum)
        a1, a2 = countVictories(new_p1, new_p2, new_current_player)
        v1 += a1*n_universes
        v2 += a2*n_universes
    
    return v1, v2
