from utils import import_diagnostic_matrix

diagnostic_path = "./data/input"
diagnostic = import_diagnostic_matrix(diagnostic_path)

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
