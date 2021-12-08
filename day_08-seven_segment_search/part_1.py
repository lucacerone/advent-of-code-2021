from utils import (
    import_data,
    is_1, is_4, is_7, is_8
)

data = import_data("./data/input")

def count_number(x):
    return is_1(x) or is_4(x) or is_7(x) or is_8(x)

counter = 0
for _, output in data:
    for val in output:
        if count_number(val):
            counter+=1

print(f"There are {counter} digits in [1,4,7,8]")
