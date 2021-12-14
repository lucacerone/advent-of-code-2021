from utils import (
    import_data,
    make_polymers_rules,
    make_bigrams_rules,
    count_polymers,
    count_bigrams,
    apply_polymers_rules,
    apply_bigrams_rules
)

path = "./data/input"

template, insertions = import_data(path)
polymers_rules = make_polymers_rules(insertions)
bigrams_rules = make_bigrams_rules(insertions)

polymers = count_polymers(template)
bigrams = count_bigrams(template)

for i in range(40):
    polymers = apply_polymers_rules(polymers, bigrams, polymers_rules)
    bigrams = apply_bigrams_rules(bigrams, bigrams_rules)

difference = max(polymers.values()) - min(polymers.values())

print(difference, "= max(val) - min(val)")
