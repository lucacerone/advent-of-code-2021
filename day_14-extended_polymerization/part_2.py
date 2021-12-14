from utils import (
    import_data,
    make_bigram_to_new_polymer_mapping,
    make_bigrams_rules,
    count_polymers,
    count_bigrams,
    update_polymers_count,
    update_bigrams_count
)

path = "./data/input"

template, insertions = import_data(path)
bigram_to_new_polymer = make_bigram_to_new_polymer_mapping(insertions)
bigrams_rules = make_bigrams_rules(insertions)

polymers = count_polymers(template)
bigrams = count_bigrams(template)

for i in range(40):
    polymers = update_polymers_count(polymers, bigrams, bigram_to_new_polymer)
    bigrams = update_bigrams_count(bigrams, bigrams_rules)

difference = max(polymers.values()) - min(polymers.values())

print(f"Solution: {difference}")
