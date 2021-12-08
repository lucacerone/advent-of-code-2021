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


from functools import reduce
from collections import defaultdict

class DigitDecoder:
    """
    A DigitDecoder class is instantiated using the 10 inputs for a specific display.
    
    The decoder finds the inverse mapping to decode the outputs using the following:
    
    - the numbers 1 and 4 can be identified just by looking at the number of segments making the digit
      (as explained in the challenge description)
    
    - when looking at all the 10 digits, some segments can be identified just by looking at the frequency

    - combining the frequency of the segments and the knowledge of digits from the number of segments they are made of, 
      can be used to further disambiguate some of the segments

    To illustrate the strategy used, consider the following diagram ("x" means the digit uses the segment, "." means the segment is not used):      

            a  b  c  d  e  f  g   num-segments
          |--------------------
        0 | x  x  x  .  x  x  x   6
        1 | .  .  x  .  .  x  .   2
        2 | x  .  x  x  x  .  x   5
        3 | x  .  x  x  .  x  x   5
        4 | .  x  x  x  .  x  .   4
        5 | x  x  .  x  .  x  x   5
        6 | x  x  .  x  x  x  x   6
        7 | x  .  x  .  .  x  .   3
        8 | x  x  x  x  x  x  x   7
        9 | x  x  x  x  .  x  x   6
          |
    freq: | 8  6  8  7  4  9  7

    Using the diagram above, we can find how the different settings have been mapped with the following strategy:
    - identify the numbers 1, 4, using number of segments (to disambiguate the mapping, 7 and 8 are not needed)
    - the segment appearing 4 times maps to "e"
    - the segment appearing 6 times maps to "b"
    - the segment appearing 9 times maps to "f"
    - the segment appearing 7 times and used by 4 maps to "d"
    - the segment appearing 7 times and not used by 4 maps to "g"
    - the segment appearing 8 times and used by 1 maps to "c"
    - the segment appearing 8 times but not used by 1 maps to "a"

    With this mapping we can decode the output to a "canonic form" (segments used in alphabetical order)
    and get the corresponding digit from the SEGMENTS_TO_DIGIT dictionary.

    """
    def __init__(self, inputs:list[str]) -> None:
        self._inputs = inputs
        self._mapping = self._find_mapping()
    
    def _find_mapping(self):
        segments_1 = self._get_segments_1()
        segments_4 = self._get_segments_4()
        count_to_segment_candidates = self._get_count_to_segment_candidates()

        maps_to_e = self._get_singleton_element(count_to_segment_candidates[4])
        maps_to_b = self._get_singleton_element(count_to_segment_candidates[6])
        maps_to_f = self._get_singleton_element(count_to_segment_candidates[9])
        maps_to_d = self._get_singleton_element(count_to_segment_candidates[7] & segments_4)
        maps_to_g = self._get_singleton_element({c for c in count_to_segment_candidates[7] if c not in segments_4})
        maps_to_c = self._get_singleton_element(count_to_segment_candidates[8] & segments_1)
        maps_to_a = self._get_singleton_element({c for c in count_to_segment_candidates[8] if c not in segments_1})

        return {
            maps_to_a: "a",
            maps_to_b: "b",
            maps_to_c: "c",
            maps_to_d: "d",
            maps_to_e: "e",
            maps_to_f: "f",
            maps_to_g: "g"
        }
    
    def __call__(self, output: list[str]) -> int:
        powers = range(len(output)-1, -1, -1)
        value = 0
        for i, segments in enumerate(output):
            value += self._to_digit(segments) * 10 ** powers[i]
        return value
    
    def _to_digit(self, digit_segments):
        segments = self._decode_to_canonic_form(digit_segments)
        return SEGMENTS_TO_DIGIT[segments]
    
    def _decode_to_canonic_form(self, digit_segments):
        decoded = ""
        for s in digit_segments:
            decoded += self._mapping[s]
        return canonic_form(decoded)
    
    def _combine_inputs(self):
        return reduce(lambda x,y: x+y, self._inputs)

    def _get_segments_counts(self):
        all_segments = self._combine_inputs()
        segments_counts = defaultdict(int)
        for s in all_segments:
            segments_counts[s] +=1
        return segments_counts
    
    def _get_count_to_segment_candidates(self):
        segment_counts = self._get_segments_counts()
        counts_to_candidates = defaultdict(set)
        for s in segment_counts:
            counts_to_candidates[segment_counts[s]].add(s)
        return counts_to_candidates
    
    def _get_segments_1(self):
        return set([i for i in self._inputs if is_1(i)][0])
    
    def _get_segments_4(self):
        return set([i for i in self._inputs if is_4(i)][0])
    
    @staticmethod
    def _get_singleton_element(s):
        if len(s) != 1:
            raise ValueError(f"Expecting a set with one element, got {s}")
        return s.copy().pop()
