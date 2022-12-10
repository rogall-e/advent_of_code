import string

with open('2022/input_files/day3.txt') as f:
    test_lines = f.read()

def get_data(data):    
    data = data.split('\n')
    return data

data = get_data(test_lines)

def calc_priority(letter_list):
    double_letters = letter_list
    low_alphabet = list(string.ascii_lowercase)
    priority = []
    for item in double_letters:
        for idx,letter in enumerate(low_alphabet):
            if letter.lower() == item:   
                priority.append(idx+1)
            if letter.upper() == item:     
                priority.append(idx+27)        
    return sum(priority)

def check_double_items(data):
    rucksack_compartments = [(x[:int(len(x)/2)],x[int(len(x)/2):]) for x in data]
    double_letters = []
    for rucksack in rucksack_compartments:
        double_letter = set(x for x in rucksack[0] if x in rucksack[1]).pop()
        double_letters.append(double_letter) 
    priority = calc_priority(double_letters)
    return priority

def calc_batches(data):
    double_letters = []
    l = len(data)
    for ndx in range(0, l, 3):
        batch = data[ndx:min(ndx + 3, l)]
        double_letter = set(x for x in batch[0] if x in batch[1] and x in batch[2]).pop()
        double_letters.append(double_letter)
    priority = calc_priority(double_letters)
    return priority

print(check_double_items(data))
print(calc_batches(data))


