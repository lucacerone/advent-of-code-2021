import fileinput
import utils as u

completion_scores = []

for line in fileinput.input("./data/input"):
    line = line.rstrip()
    if not u.is_corrupted(line):
        completion_sequence = u.complete_sequence(line)
        completion_scores.append(u.score_completing_sequence(completion_sequence))

completion_scores.sort()
n_scores = len(completion_scores)

middle_idx = (n_scores -1) // 2
middle_score = completion_scores[middle_idx]
print(f"The middle autocompletion score is {middle_score}")
