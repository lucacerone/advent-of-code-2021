from collections import namedtuple

PlayerState = namedtuple("PlayerState",["position", "score"])

def deterministic_die():
    values = list(range(1,101))
    i=0
    while True:
        indices = [idx % 100 for idx in range(i, i+3)]
        rolls = [values[idx] for idx in indices]
        i = (i+3) % 100
        yield rolls
        
def update_player_state(player, rolled):
    steps = sum(rolled)

    new_position = (player.position + steps) % 10
    new_position = new_position if new_position else 10
    
    new_score = player.score + new_position

    return PlayerState(position=new_position, score=new_score)


