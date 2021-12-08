from utils import import_initial_states
from lanternfish import LanterfishSchoolAggregated

initial_states = import_initial_states("./data/input")

school = LanterfishSchoolAggregated(initial_states)

for i in range(256):
    school.age()
    if i == 79:
        print(f"After 80 days there are {school.size()} fishes.")

print(f"After 256 days there are {school.size()} fishes.")
