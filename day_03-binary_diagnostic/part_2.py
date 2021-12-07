import fileinput
from utils import import_diagnostic_matrix

def most_common_value(diagnostic, pos):
    position_values = diagnostic[:, pos]
    n_values = diagnostic.shape[0]

    return 1 if position_values.sum() >= n_values / 2 else 0


def least_common_value(diagnostic, pos):
    position_values = diagnostic[:, pos]
    n_values = diagnostic.shape[0]

    return 0 if position_values.sum() >= n_values / 2 else 1


def filter_binary_code(diagnostic, criteria_fun):
    n_cols = diagnostic.shape[1]

    codes = diagnostic.copy()
    for pos in range(n_cols):
        value = criteria_fun(codes, pos)
        codes = codes[codes[:,pos] == value]

        if codes.shape[0] == 1:
            break
    return codes[0,:]

def binary_array_to_decimal(binary_array):
    return int("".join(map(str, binary_array)),2)

diagnostic = import_diagnostic_matrix("./data/input")

oxygen_generator_rating = binary_array_to_decimal(
    filter_binary_code(diagnostic, most_common_value)
)

co2_scrubber_rating = binary_array_to_decimal(
    filter_binary_code(diagnostic, least_common_value)
)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating

print("Oxygen Generator Rating", oxygen_generator_rating)
print("CO2 Scrubber Rating", co2_scrubber_rating)
print("Life Support Rating", life_support_rating)

