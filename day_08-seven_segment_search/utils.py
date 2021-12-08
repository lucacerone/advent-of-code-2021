def canonic_form(x):
    return "".join(sorted(x))

def import_data(path):
    data = []
    with open(path, "r") as fh:
        for line in fh:
            line = line.rstrip()
            inputs, outputs = line.split("|")
            inputs = inputs.strip().split(" ")
            outputs = outputs.strip().split(" ")
            data.append((inputs, outputs))
    return data

def is_1(x):
    return len(x) == 2

def is_4(x):
    return len(x) == 4

def is_7(x):
    return len(x) == 3

def is_8(x):
    return len(x) == 7
