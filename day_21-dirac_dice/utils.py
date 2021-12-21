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

@cache
def update_player_state(player, rolled):
    dice_sum = sum(rolled)
    return update_player_state_from_dice_sum(player, dice_sum)


@cache
def update_player_state_from_dice_sum(player, dice_sum):
    new_position = (player.position + dice_sum) % 10
    new_position = new_position if new_position else 10
    
    new_score = player.score + new_position

    return PlayerState(position=new_position, score=new_score)


### CODE FOR PART 2

POSSIBLE_ROLLS_ = itertools.product(range(1,4), range(1,4), range(1,4))

POSSIBLE_SUMS = {}
for s in map(sum, POSSIBLE_ROLLS_):
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
    return update_player_state_from_dice_sum(p1, p2, current_player, dice_sum)

"""
# OLD IMPLEMENTATION
@cache
def countVictories(p1, p2, current_player, SCORE_TO_WIN=21):
    if current_player == 1:
        if p1.score >= SCORE_TO_WIN:
            return (1, 0)
        else:
            v1, v2 = 0,0
            for dice_sum, n_universes in POSSIBLE_SUMS.items():
                p1, p2, next_player = update_game_state_from_dice_sum(p1, p2, current_player, dice_sum)
                p1_victories, p2_victories = countVictories(p1, p2,next_player, SCORE_TO_WIN)
                v1 += n_universes*p1_victories
                v2 += n_universes*p2_victories
            return v1, v2
    else:
        if p2.score >= SCORE_TO_WIN:
            return (0, 1)
        else:
            v1, v2 = 0,0
            for dice_sum, n_universes in POSSIBLE_SUMS.items():
                p1, p2, next_player = update_game_state_from_dice_sum(p1, p2, current_player, dice_sum)
                p1_victories, p2_victories = countVictories(p1, p2,next_player, SCORE_TO_WIN)
                v1 += n_universes*p1_victories
                v2 += n_universes*p2_victories
            return v1,v2
"""

def countVictories(p1, p2, current_player, SCORE_TO_WIN=21):

