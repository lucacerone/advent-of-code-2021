from utils import import_initial_states
from lanternfish import LanterfishSchool

initial_states = import_initial_states("./data/input")

school = LanterfishSchool(initial_states)

for i in range(80):
    school.age()

print(f"After 80 days there are {school.size()} fishes.")
