from collections import Counter, defaultdict

with open('data/day14.txt') as f:
    data_input = f.read()

test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def get_input(data):
    data = data.split('\n')
    data = [x.strip() for x in data if x]
    polymer_string = data[0]
    data = data[1:]
    data = [x.split(' -> ') for x in data]
    
    polymer_rules = {}
    for element in data:
        element_tuple = tuple(element[0])
        polymer_rules[element_tuple] = element[1]
        
    polymer_combinations = defaultdict(int)
    for idx in range(len(polymer_string) -1):
        char_combi = (polymer_string[idx],  polymer_string[idx+1])
        polymer_combinations[char_combi] += 1
    
    polymer_count = Counter(polymer_string)

    return polymer_rules, polymer_combinations, polymer_count


def reaction(data, number_of_reactions):
    polymer_rules, polymer_combinations, polymer_count = get_input(data)
    counter = 0
    while counter < number_of_reactions:
        updated_polymer = defaultdict(int)
        for combination, count in polymer_combinations.items():
            polymer_count[polymer_rules[combination]] += count
            updated_polymer[combination[0], polymer_rules[combination]] += count
            updated_polymer[polymer_rules[combination], combination[1]] += count
        polymer_combinations = updated_polymer
        counter += 1
    return max(polymer_count.values()) - min(polymer_count.values())
        
    

print(reaction(data_input,40))
