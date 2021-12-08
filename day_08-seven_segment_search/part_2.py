from utils import import_data
from digits import decode

data = import_data("./data/input")

decoded_outputs = [decode(inputs, outputs) for inputs, outputs in data]

print(f"The sum of decoded outputs is {sum(decoded_outputs)}")
