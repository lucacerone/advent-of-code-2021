from utils import parse_reading

input_file = "./data/input"

previous_reading = None
increased=0

with open(input_file, "r") as fh:
    for input in fh:
        current_reading = parse_reading(input)

        if previous_reading and current_reading > previous_reading:
            increased += 1
            
        previous_reading = current_reading

print(f"Detected {increased} increases")
