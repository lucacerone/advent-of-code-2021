import utils as u


h = '38006F45291200'
#h = u.import_data("./data/input")
b = u.hex_to_bin(h)

parsed = []
versions = []

while b:
    v = u._version(b)
    versions.append(v)
    t = u._type_id(b)

    if t == 4:
        res = u.literal_operator(b)
    else:
        res = u.other_operator(b)

    b=b[res["current_idx"]:]

