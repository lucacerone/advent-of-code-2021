from utils import import_data
from digits import DigitDecoder

data = import_data("./data/input")

decoded_outputs = []
for inputs, outputs in data:
    decode = DigitDecoder(inputs)
    decoded_outputs.append(decode(outputs))

print(f"The sum of decoded outputs is {sum(decoded_outputs)}")
