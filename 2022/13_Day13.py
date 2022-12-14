import ast
import functools

with open('2022/input_files/day13.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    data = [x.strip() for x in data]
    return data

test_data = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

data = get_data(lines)
data = [ast.literal_eval(x) for x in data if x != '']

def comp(l1, l2):
    for (a,b) in zip(l1, l2):
        aint = isinstance(a, int)
        bint = isinstance(b, int)
        if aint and bint:
            cmp = a-b
        elif not aint and not bint:
            cmp = comp(a, b)
        elif aint:
            cmp = comp([a], b)
        else:
            cmp = comp(a, [b])
        if cmp:
            return cmp
    return len(l1) - len(l2)



pairs = [[data[i], data[i+1]] for i in range(0,len(data)-1,2)]

part1 = 0
for idx,(l,r) in enumerate(pairs):
    if comp(l,r) < 0:
        part1 += idx+1
  
print(part1)
    


 
    
