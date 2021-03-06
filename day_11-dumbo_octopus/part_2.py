import io
import utils as u
import numpy as np

data = u.import_data("./data/input")

step=0
while True:
    """
    - Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1, 
      including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes. 
      This process continues as long as new octopuses keep having their energy level increased beyond 9. (An octopus can only flash at most once per step.)
    - Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
    """
    step += 1
    
    # First, the energy level of each octopus increases by 1.
    data = data + 1


    # Then, any octopus with an energy level greater than 9 flashes.
    can_flash = {(x,y) for x,y in np.argwhere(data>9)}
    flashed = set()

    while can_flash:
        pos = can_flash.pop()
        flashed.add(pos)

        pos_neigh = u.get_neighbors_positions(data, pos)
        for pn in pos_neigh:
            data[pn] = min(data[pn] + 1,10)
                        
            if data[pn] > 9 and pn not in flashed:
                can_flash.add(pn)

    for i,j in flashed:
        data[i,j] = 0

    if len(flashed) == 100:
        break

print(f"The first time all dumbo octopus flash togethe is {step}.")

