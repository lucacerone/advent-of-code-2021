from heapq import heappush, heappop
import utils as u

initial_cost = 0
initial_configuration = u.Configuration(
  hallway = u.Hallway(('.',)*11),
  rooms = {
    "A": u.Room(('D','D','D','C'), "A", 2),
    "B": u.Room(('B','C','B','A'), "B", 4),
    "C": u.Room(('A','B','A','D'), "C", 6),
    "D": u.Room(('C','A','C','B'), "D", 8),
  }
)


final_configuration = u.Configuration(
  hallway = u.Hallway(('.',)*11),
  rooms = {
    "A": u.Room(('A','A','A','A'), "A", 2),
    "B": u.Room(('B','B','B','B'), "B", 4),
    "C": u.Room(('C','C','C','C'), "C", 6),
    "D": u.Room(('D','D','D','D'), "D", 8),
  }
)

costs_configuration = {
  initial_configuration: initial_cost
}

visited = set()
to_visit = [(initial_cost, initial_configuration)]

while to_visit:
  if final_configuration in visited:
    break

  current_cost, current_configuration = heappop(to_visit)
  if current_configuration in visited:
    continue

  for transition_cost, next_configuration in current_configuration.next_configurations():
    new_cost = current_cost + transition_cost

    if next_configuration not in costs_configuration or new_cost < costs_configuration[next_configuration]:
      costs_configuration[next_configuration] = new_cost
      heappush(to_visit, (new_cost, next_configuration))

  visited.add(current_configuration)

print("Solution:", costs_configuration[final_configuration])
