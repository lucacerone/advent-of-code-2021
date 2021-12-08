from utils import is_1, is_4, is_7, is_8

def canonic_form(x):
    return "".join(sorted(x))

SEGMENTS_TO_DIGIT = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

def find_mapping(inputs):
    # find 1 and 7, the segment in 7 but not in 1 should be mapped to "a"
    segments_1 = set([x for x in inputs if is_1(x)][0])
    segments_7 = set([x for x in inputs if is_7(x)][0])
    segments_4 = set([x for x in inputs if is_4(x)][0])
    segments_8 = set([x for x in inputs if is_8(x)][0])
    maps_to_a = (segments_7 - segments_1).pop()

    # 6 is the only 6 segment digit that has only 1 segment in common with 1 (which should map to "f")
    six_segments_digits = [set(x) for x in inputs if len(x) == 6]
    segments_6 = set([six for six in six_segments_digits if len(six.intersection(segments_1)) == 1][0])
    maps_to_f = segments_6.intersection(segments_1).pop()

    # After determining which segment of 1 maps to "c", we can infer that the other segment maps to "c"
    maps_to_c = (segments_1 - set(maps_to_f)).pop()

    # 9 is the only 6 segments digit, that contains the same segments as 4
    # Removing 9 segments from 8 segments gives the mapping to the segment "e"
    segments_9 = [nine for nine in six_segments_digits if segments_4.issubset(nine)][0]
    maps_to_e = (segments_8 - segments_9).pop()

    # the remaining six segments digit is the 0:
    segments_0 = [
        zero
        for zero in six_segments_digits
        if zero != segments_6 and zero != segments_9
    ][0]

    # removing segments of 0 from 8, gives the segment that maps to "d"
    maps_to_d = (segments_8 - segments_0).pop()

    # We can find which segments maps to "g" by subtracting from 6 the segments for 4, plus the segments for a and e
    # (which we have already identified)
    maps_to_g = (segments_6 - segments_4 - set([maps_to_a, maps_to_e])).pop()

    # Finally, we can find which segment maps to b, by subtracting from 4 the segments mapping c, d, and f
    maps_to_b = (segments_4 - set([maps_to_c, maps_to_d, maps_to_f])).pop()

    mapping = {
        maps_to_a: "a",
        maps_to_b: "b",
        maps_to_c: "c",
        maps_to_d: "d",
        maps_to_e: "e",
        maps_to_f: "f",
        maps_to_g: "g",
    }

    return mapping

def apply_mapping(value, mapping):
    mapped = "".join([mapping[l] for l in value])
    return canonic_form(mapped)

def decode_digit(value, mapping):
    digit_segments = apply_mapping(value, mapping)
    return SEGMENTS_TO_DIGIT[digit_segments]

def digits_to_integer(digits):
    return int("".join([str(digit) for digit in digits]))

def decode(inputs, outputs):
    mapping = find_mapping(inputs)
    digits = [decode_digit(value,mapping) for value in outputs]
    return digits_to_integer(digits)
