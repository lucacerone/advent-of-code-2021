def import_initial_states(path):
    with open(path, "r") as fh:
        state = fh.readline().rstrip()
    
    state = [int(x) for x in state.split(",")]
    return state
