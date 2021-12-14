def import_data(path):
    with open(path,"r") as fh:
        template = fh.readline().rstrip()
        
        insertions = []
        for line in fh:
            if line == "\n":
                continue
        
            line = line.rstrip()
            pair, char = line.split(" -> ")
            insertions.append((pair, char))
    
    return template, insertions

def polymer_bigrams_iter(template):
    n = len(template) -1
    for i in range(n):
        yield template[i] + template[i+1]

def count_polymers(template):
    polymers = dict()
    for p in template:
        polymers[p] = polymers.get(p,0) +1
    return polymers

def count_bigrams(template):
    counter = dict()
    for bigram in polymer_bigrams_iter(template):
        counter[bigram] = counter.get(bigram,0) + 1
    return counter

def make_polymers_rules(insertions):
    rules = dict()
    for bigram, polymer in insertions:
        rule = (polymer, 1)
        rules[bigram] = rule
    return rules

def make_bigrams_rules(insertions):
    rules = dict()

    for bigram, polymer in insertions:
        left, right = bigram
        rule = dict()
        rule[left+polymer] = 1
        rule[polymer+right] = 1
        rule[bigram] = rule.get(bigram,0) -1
        if rule[bigram] == 0:
            del rule[bigram]
        rules[bigram] = rule

    return rules

def apply_polymers_rules(polymers, bigrams, polymers_rules):
    polymers = polymers.copy()
    for b, nb in bigrams.items():
        p, val = polymers_rules[b]
        polymers[p] = polymers.get(p,0) + nb*val
    return polymers

def apply_bigrams_rules(bigrams, bigrams_rules):
    bigrams = bigrams.copy()
    current_bigrams = list(bigrams.items())
    for b, nb in current_bigrams:
        rule = bigrams_rules[b]
        
        for to_update, amount in rule.items():
            new_count = bigrams.get(to_update,0) + nb*amount
            
            if new_count == 0:
                del bigrams[to_update]
            else: 
                bigrams[to_update] = new_count
    return bigrams
