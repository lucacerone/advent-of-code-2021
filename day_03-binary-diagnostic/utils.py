import fileinput

import numpy as np

def import_diagnostic_matrix(diagnostic_path):

    diagnostic = []
    for line in fileinput.input(diagnostic_path):
        record = line.rstrip()
        bits = list(map(lambda x: int(x), record))
        diagnostic.append(bits)

    diagnostic = np.array(diagnostic)
    return diagnostic
