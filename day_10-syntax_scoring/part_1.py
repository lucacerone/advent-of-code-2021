import utils as u

with open("./data/input","r") as fh:
    corrupted_counts = u.first_corrupted_bracket_counts(fh)

score = u.score_syntax_error(corrupted_counts)

print(f"Syntax Error Score: {score}")
