from collections import defaultdict


with open('2022/input_files/day5.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    return data

data = get_data(lines)

def preprocess_data(data):
    crates = []
    moves = []
    for x in data:
        if not x.startswith('move') and x != '':
            crates.append(x)
        if x.startswith('move'):
            moves.append(x)   

    moves = [x.split(' ') for x in moves]
    
    crate_idx = []       
    crate_dict = defaultdict(list)
    for item in crates:
        if not item.startswith(' 1'):
            for i,letter in enumerate(item):
                if letter != ' ' and letter != '[' and letter != ']':  
                    crate_dict[f'{i}'].append(letter)
        if item.startswith(' 1'):
            for i,letter in enumerate(item):
                if letter != ' ':
                    crate_idx.append((i, letter))
                    
    for old,new in crate_idx:
        crate_dict[new] = crate_dict.pop(str(old))
        
    return moves, crate_dict



def part_1(data):
    moves, crate_dict = preprocess_data(data)
    
    for move in moves:
        for _ in range(int(move[1])):
            crate_move = crate_dict[move[3]].pop(0)
            crate_dict[move[5]].insert(0, crate_move)
            
    solution = ''
    for key in sorted(crate_dict):
        solution += f"{crate_dict[key][0]}"
        
    return solution


def part_2(data):
    moves, crate_dict = preprocess_data(data)
    
    for move in moves:
        for _ in range(int(move[1])):
                crate_move = crate_dict[move[3]].pop(0)
                crate_dict[move[5]].insert(_, crate_move)
                
    solution = ''
    for key in sorted(crate_dict):
        solution += f"{crate_dict[key][0]}"
        
    return solution            
    
            
print(part_1(data))
print(part_2(data))