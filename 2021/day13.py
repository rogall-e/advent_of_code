import numpy as np


with open('data/day13.txt') as f:
    data = f.readlines()

test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

def get_data(data):
    data = [x.replace('\n', '') for x in data]
    folding_lst = [x.replace('fold along ', '') for x in data if x.startswith('fold')]
    data = [x for x in data if not x.startswith('fold')]
    data.remove('')
    data= [x.split(',') for x in data]
    folding_lst = [x.split('=') for x in folding_lst]
    folding_lst = [{k:int(v)} for k,v in folding_lst]
    return data, folding_lst

def get_test_data(data):
    data = data.split('\n')
    folding_lst = [x.replace('fold along ', '') for x in data if x.startswith('fold')]
    data = [x for x in data if not x.startswith('fold') and x != '']
    data= [x.split(',') for x in data]
    folding_lst = [x.split('=') for x in folding_lst]
    folding_lst = [{k:int(v)} for k,v in folding_lst]
    return data, folding_lst

def get_points(data):
    data, folding_lst = get_data(data)
    points = []
    for item in data:
        points.append((int(item[0]), int(item[1])))
    return points, folding_lst

def get_transparent_paper(data):
    points, folding_lst = get_points(data)
    width = max(points, key = lambda i : i[0])[0] + 1
    length = max(points, key = lambda i : i[1])[1] + 1
    paper = np.arange(width * length).reshape(length, width)
    paper = np.full_like(paper, 0)
    return paper

def get_dots(data, part_1 = True, part_2 = False):
    points, folding_lst = get_points(data)
    paper = get_transparent_paper(data)
    dots = 0
    for point in points:
        paper[point[1], point[0]] = 1
    counter = 0
    for item in folding_lst:
        counter += 1
        for k,v in item.items():
            if k == 'y':
                upper_paper, lower_paper = np.split(paper, [v], axis=0)
                lower_paper = np.delete(lower_paper, 0, axis=0)
                lower_paper = np.flip(lower_paper, 0)
                if len(lower_paper) < len(upper_paper):
                    diff = abs(len(lower_paper) - len(upper_paper))
                    lower_paper = np.pad(lower_paper, ((diff,0), (0,0),), mode='constant', constant_values=0)
                elif len(lower_paper) > len(upper_paper):
                    diff = abs(len(lower_paper) - len(upper_paper))
                    upper_paper = np.pad(upper_paper, ((0,diff), (0,0),), mode='constant', constant_values=0)
                new_paper = upper_paper + lower_paper
                paper = new_paper
                dots = np.count_nonzero(paper > 0)
                #print('Upper paper: \n', upper_paper, '\nLower_paper: \n', lower_paper, '\nNew paper: \n', new_paper)
                #print('Dots:', dots ,'\n')
            if k == 'x':
                left_paper, right_paper = np.split(paper, [v], axis=1)
                right_paper = np.delete(right_paper, 0, axis=1)
                right_paper = np.flip(right_paper, 1)
                if len(right_paper[0]) > len(left_paper[0]):
                    diff = abs(len(right_paper[0]) - len(left_paper[0]))
                    right_paper = np.pad(right_paper, ((0,0), (0, diff),), mode='constant', constant_values=0)
                elif len(right_paper[0]) < len(left_paper[0]):
                    diff = abs(len(right_paper[0]) - len(left_paper[0]))
                    left_paper = np.pad(left_paper, ((0,0), (diff, 0),), mode='constant', constant_values=0)
                new_paper = left_paper + right_paper
                paper = new_paper
                dots = np.count_nonzero(paper > 0)
                #print('Left paper: \n', left_paper, '\nRight_paper: \n', right_paper, '\nNew paper: \n', new_paper)
                #print('Dots:', dots ,'\n')
        if counter == 1 and part_1:
            return dots
            break
    if part_2:
        paper[paper > 0] = 1
        paper_lst = paper.tolist()
        return (
            "\n ".join(" ".join(map(str, row)) for row in paper_lst) \
                .replace('0', '.') \
                .replace('1', '#')
            )
              
    

print('Result Part1:', get_dots(data))
print('Result Part2:\n', get_dots(data, False, True))

