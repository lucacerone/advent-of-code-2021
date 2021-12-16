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

def _version(chunk):
    return int(chunk[:3],2)

def _type_id(chunk):
    return int(chunk[3:6],2)


def get_chunks(message):
    while message: 
        print("message:", message)
        type_id = int(message[3:6],2)
        if type_id == 4:
            chunk = message[:24]
            message = message[24:]
            yield chunk
        else:
            print("in else")
            message = message[24:]

def literal_operator(chunk):
    assert len(chunk) % 4 == 0 
    version = _version(chunk)
    type_id = _type_id(chunk)

    digits = []

    last_digit = False
    i = 0
    while not last_digit:
        left, right = 6+5*i, 6+5*(i+1)
        bd = chunk[left:right]
        digits.append(bd[1:])
        last_digit = bd[0] == '0'
        i+=1
    print(6+5*i)

    value = int("".join(digits),2)

    return {
        "version": version,
        "type_id": type_id,
        "value": value
    }




type_id_to_operator = {
    4: literal_operator
}
