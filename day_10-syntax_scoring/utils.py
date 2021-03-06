from collections import defaultdict

BRACKETS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

OPENING_BRACKETS = {k for k in BRACKETS.keys()}
CLOSING_BRACKETS = {v for v in BRACKETS.values()}

POINTS_ILLEGAL = {")": 3, "]": 57, "}": 1197, ">": 25137}

POINTS_COMPLETION = {")": 1, "]": 2, "}": 3, ">": 4}

def is_opening_bracket(bracket):
    return bracket in OPENING_BRACKETS

def is_closing_bracket(bracket):
    return bracket in CLOSING_BRACKETS


def first_corrupted_bracket(line):
    """
    A line is corrupted if one of its chunks terminates with the wrong bracket.

    This function finds the first illegal bracket.
    """

    opened = []
    for bracket in line:
        if is_opening_bracket(bracket):
            opened.append(bracket)
        elif is_closing_bracket(bracket):
            current_open = opened.pop()
            expected = BRACKETS[current_open]
            if  expected != bracket:
                return bracket, expected
        else:
            raise ValueError(f"Unexpected character {bracket}")
    return None, None

def is_corrupted(line):
    corrupted, _ = first_corrupted_bracket(line)
    return corrupted is not None

def first_corrupted_bracket_counts(stream):
        corrupted_counts = defaultdict(int)
        for line in stream:
            line = line.rstrip()
            corrupted, _ = first_corrupted_bracket(line)            
            if corrupted:
                corrupted_counts[corrupted] += 1
        return corrupted_counts

def score_syntax_error(corrupted: dict):
    value = 0
    for bracket, count in corrupted.items():
        value += POINTS_ILLEGAL[bracket] * count
    return value

def complete_sequence(line):
    expected = []
    for bracket in line:
        if is_opening_bracket(bracket):
            expected.append(BRACKETS[bracket])
        elif is_closing_bracket(bracket):
            expected.pop()
        else:
            raise ValueError(f"Unexpected character {bracket}")
    return "".join(expected[::-1])

def score_completing_sequence(sequence):
    value = 0
    for bracket in sequence:
        value *= 5
        value += POINTS_COMPLETION[bracket]
    return value

