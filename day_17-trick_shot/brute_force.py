Txmin, Txmax = 48, 70
Tymin, Tymax = -189, -148


"""
X_{0} = 0
Y_{0} = 0
Vx_{0} = ?
Vy_{0} = ?

X_{n+1} = X_{n} + Vx_{n}
Y_{n+1} = Y_{n} + Vy_{n}
Vx_{n+1} = Vx_{n} -1 if Vx_{n} > 0 else 0 (consider only positive velocities for now)
Vy_{n+1} = Vy_{n} -1


MaxX position = Vx_0 * (Vx_0 + 1)/2, 
To land the target we must have Txmin <= MaxX <= Txmax 

MaxY position = Vy_0 * (Vy_0 + 1)/2
MaxY position reached after Vy_0 steps. At Vy+1 probe has the same height

Descent starts at ()

"""


TARGET_X_MIN, TARGET_MAX_X = 48, 70
TARGET_Y_MIN, TARGET_Y_MAX = -189, -148

# Vx >= 10 #math.ceil((-1 + math.sqrt(1+4*2*48))/2) obtained plugging MaxX formula (Vx0*(Vx0+1)/2 in inequality above) # note, this only works in some circumstances (specifically target being in the 4th quadrant)
# Vx <= 11 #math.floor((-1 + math.sqrt(1+4*2*70))/2)

def update_vx(vx):
    if vx > 0:
        return vx-1
    elif vx == 0:
        return vx
    elif vx < 0:
        return vx + 1
    else:
        raise ValueError("Unknown situation: vx =", vx)


def update_vy(vy):
    return vy - 1
    

def step(pos, v):
    return [(pos[0] + v[0], pos[1] + v[1]), (update_vx(v[0]), update_vy(v[1]))]


def horizontal_stop_time(initial_velocity):
    return abs(initial_velocity[0])


def max_horizontal_position(initial_velocity):
    x0 = initial_velocity[0]
    return x0*(x0+1)//2


def max_height(initial_velocity):
    return initial_velocity[1]*(initial_velocity[1]+1)//2 if initial_velocity[1] else 0


def max_height_first_time(initial_velocity):
    initial_vertical_velocity = initial_velocity[1]
    return initial_vertical_velocity if initial_vertical_velocity > 0 else 0


def descent_start_time(initial_velocity):
    y0 = initial_velocity[1]
    return 0 if y0 < 0 else max_height_first_time(initial_velocity) + 1


def in_target(pos):
    return  TARGET_X_MIN <= pos[0] <= TARGET_MAX_X and TARGET_Y_MIN <= pos[1] <= TARGET_Y_MAX


def past_target(pos):
    return pos[0] > TARGET_MAX_X or pos[1] < TARGET_Y_MIN



valid_initial_positions = []

m_h = 0
for vx0 in range(TARGET_MAX_X+1):
    for vy0 in range(TARGET_Y_MIN, -TARGET_Y_MIN):
        initial_velocity = (vx0, vy0)
        pos, velocity = (0,0), initial_velocity
        keep_going = True
        while keep_going:
            pos, velocity = step(pos, velocity)

            if in_target(pos):
                m_h = max(m_h, max_height(initial_velocity))
                valid_initial_positions.append((initial_velocity))
                keep_going = False
            elif past_target(pos):
                keep_going = False
            else:
                pass

print(f"Part 1: max height = {m_h}")
print(f"Part 2: n_trajectories = {len(valid_initial_positions)}")
