import fileinput
import numpy as np

diagnostic_path = "./data/input"

diagnostic = []
for line in fileinput.input(diagnostic_path):
    record = line.rstrip()
    bits = list(map(lambda x: int(x), record))
    diagnostic.append(bits)

diagnostic = np.array(diagnostic)

n_rows = diagnostic.shape[0]
code = diagnostic.sum(axis=0)

gamma_rate_binary = list(map(lambda x: 1 if x else 0, (code > n_rows/2)))
epsilon_rate_binary = [1 - x for x in gamma_rate_binary]



gamma_rate_binary = list(map(lambda x: str(x), gamma_rate_binary))
epsilon_rate_binary = list(map(lambda x: str(x), epsilon_rate_binary))

gamma_rate = int("".join(gamma_rate_binary),2)
epsilon_rate = int("".join(epsilon_rate_binary),2)

power_consumption = gamma_rate * epsilon_rate

print(f"Power Consumpution {power_consumption}")
