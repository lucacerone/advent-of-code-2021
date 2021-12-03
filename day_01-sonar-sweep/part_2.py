from utils import parse_reading

input_file = "./data/input"

window_size = 3

window = []

previous_sum = None
current_sum = None
increased = 0

with open(input_file, "r") as fh:
    for idx, input in enumerate(fh):
        current_reading = parse_reading(input)
        previous_window_size = len(window)
        if previous_window_size == window_size:
            window.pop(0)

        window.append(current_reading)
        current_window_size = len(window)
        
        if current_window_size < window_size:
            pass
        elif current_window_size == window_size:
            current_sum = sum(window)

            if previous_sum and current_sum > previous_sum:
                increased += 1
            previous_sum = current_sum
        else:
            raise ValueError(f"Something fishy, max window size should be: {window_size}")

print(f"Detected {increased} increases")
