from statistics import mean, median

with open("data/day10.txt") as f:
    data = f.read()

test_data = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''

test_data_2 = '''<{([{{}}[<[[[<>{}]]]>[]]
'''
    
data = data.split('\n')
data.remove('')



def find_corruption(data):
    
    pairs = {'[':']', '{':'}', '(':')', '<':'>'}
    points = {')':3, '}':1197, ']':57, '>':25137}
    corruption_stack = []
    corruption_dict = {}
    
    for idx, item in enumerate(data):
        corruption_dict[idx] = []
        for i, c in enumerate(item):
            if c in pairs:
                corruption_dict[idx].append(c)
            elif pairs[corruption_dict[idx].pop()] != c:
                corruption_stack.append(c)
    
    corruption_stack = [points[x] for x in corruption_stack]
    return sum(corruption_stack)
                


def find_idx_of_corruption(data):
    pairs = {'[':']', '{':'}', '(':')', '<':'>'}
    points = {')':3, '}':1197, ']':57, '>':25137}
    corruption_stack = []
    corruption_dict = {}
    for idx, item in enumerate(data):
        corruption_dict[idx] = []
        for i, c in enumerate(item):
            if c in pairs:
                corruption_dict[idx].append(c)
            elif pairs[corruption_dict[idx].pop()] != c:
                corruption_stack.append(idx)
    return corruption_stack

 
def complete_data(data):
    pairs = {'[':']', '{':'}', '(':')', '<':'>'}
    points = {')':1, '}':3, ']':2, '>':4}
    corruption_stack = find_idx_of_corruption(data)
    data = [item for i_drop, item in enumerate(data) if i_drop not in corruption_stack]
    
    unclosed_pairs = {}
    sequence_dict = {}
    for idx, item in enumerate(data):
        sequence_dict[idx] = []
        unclosed_pairs[idx] = []
        for i, c in enumerate(item):
            if c in pairs:
                sequence_dict[idx].append(c)
            elif pairs[sequence_dict[idx].pop()] == c:
                unclosed_pairs[idx].append(c)
        
                
    complete_sequence = {}
    for k,v in sequence_dict.items():
        complete_sequence[k] = []
        for items in v:
            pair_v = pairs[items]
            complete_sequence[k].append(pair_v)
        complete_sequence[k].reverse() 
  

    total_points = []
    for k,v in complete_sequence.items():
        points_k = 0
        v = [points[x] for x in v]
        for item in v:
            points_k = points_k * 5
            points_k += item
        total_points.append(points_k)  
        
    return median(total_points)
    
 
            
print(find_corruption(data))
print(complete_data(data))