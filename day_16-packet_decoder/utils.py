HEX_TO_BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

def import_data(path):
    with open(path,"r") as fh:
        return fh.read().rstrip()

def _hex_char_to_bin(hc):
    return HEX_TO_BIN[hc]

def hex_to_bin(h:str) -> str:
    converted = ""
    for hc in h:
        converted+=_hex_char_to_bin(hc)
    return converted

def _next_multiple_4(x):
    return 4*(x//4 + 1) if x % 4 else x

def _version(chunk):
    return int(chunk[:3],2)

def _type_id(chunk):
    return int(chunk[3:6],2)

def _length_type_id(chunk):
    return int(chunk[6],2)


def literal_operator(string):
    version = _version(string)
    type_id = _type_id(string)

    digits = []

    last_digit = False
    i = 0
    while not last_digit:
        left, right = 6+5*i, 6+5*(i+1)
        bd = string[left:right]
        digits.append(bd[1:])
        last_digit = bd[0] == '0'
        i+=1
    current_idx = 6 + 5*i
    nx4 = _next_multiple_4(current_idx)
    pad = string[current_idx:nx4]

    value = int("".join(digits),2)
    

    return {
        "version": version,
        "type_id": type_id,
        "value": value,
        "pad": pad,
        "current_idx": nx4
    }

def other_operator(message):
    version = _version(message)
    type_id = _type_id(message)
    length_type_id = _length_type_id(message)
    bits_length = 15 if length_type_id == 0 else 11
    idx = 6+ bits_length
    length = int(message[6:idx])


    return {
        "version": version,
        "type_id": type_id,
        "value": value,
        "current_idx": idx
    }


type_id_to_operator = {
    4: literal_operator
}
