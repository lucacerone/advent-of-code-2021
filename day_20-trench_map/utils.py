from collections import defaultdict

LIGHT_PIXEL = '#'
LIGHT_PIXEL_VALUE = 1

DARK_PIXEL = '.'
DARK_PIXEL_VALUE = 0



def pixel_to_val(pxl):
    if pxl == LIGHT_PIXEL: return LIGHT_PIXEL_VALUE
    elif pxl == DARK_PIXEL: return DARK_PIXEL_VALUE
    else: raise ValueError(f"Unknown pixel value '{pxl}'")

def _read_from_stream(fh):
        line = fh.readline().rstrip()

        algorithm = [pixel_to_val(pxl) for pxl in line]
        assert len(algorithm) == 512

        _ = fh.readline()

        image = dict()
        row = -1
        for line in fh:
            line = line.rstrip()
            row+=1
            col = -1
            for pxl in line:
                col += 1
                if pxl == LIGHT_PIXEL:
                    image[(row, col)] = LIGHT_PIXEL_VALUE
                elif pxl == DARK_PIXEL:
                    image[(row,col)] = DARK_PIXEL_VALUE

        return algorithm, image

def import_data(path):
    with open(path, "r") as fh:
        return _read_from_stream(fh)

def pixel_to_patch(pxl):
    x,y = pxl
    return [[(x+i, y+j) for j in (-1,0,1)] for i in (-1,0,1)]

def pixel_to_index(pxl, img, outside):
    patch = pixel_to_patch(pxl)
    values = [img.get(p, outside)  for r in patch for p in r]

    idx = 0
    for i, v in enumerate(reversed(values)):
        idx += v * 2**i

    return idx

def enhance(img, alg, outside):
    min_x = min(k[0] for k in img)
    max_x = max(k[0] for k in img)

    min_y = min(k[1] for k in img)
    max_y = max(k[1] for k in img)

    dvalue = alg[0]
    output = dict()

    for x in range(min_x-2, max_x+3):
        for y in range(min_y-2, max_y+3):
            pxl = (x,y)
            idx = pixel_to_index(pxl, img, outside)
            value = alg[idx]
            output[pxl] = value
    return output

