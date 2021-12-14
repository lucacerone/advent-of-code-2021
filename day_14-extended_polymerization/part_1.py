from utils import (
    import_data,
    make_polymers_rules,
    make_bigrams_rules,
    count_polymers,
    count_bigrams,
    update_polymers_count,
    update_bigrams_count
)

path = "./data/input"

template, insertions = import_data(path)
polymers_rules = make_polymers_rules(insertions)
bigrams_rules = make_bigrams_rules(insertions)

polymers = count_polymers(template)
bigrams = count_bigrams(template)

for i in range(10):
    polymers = update_polymers_count(polymers, bigrams, polymers_rules)
    bigrams = update_bigrams_count(bigrams, bigrams_rules)

difference = max(polymers.values()) - min(polymers.values())

print(difference, "= max(val) - min(val)")
