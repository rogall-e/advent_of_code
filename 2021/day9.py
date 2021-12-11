import numpy as np

with open("data/day9.txt") as f:
    data = f.read()


test_data = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''




def smoke_detection(data):
    small_numbers = []
    for idx,item in enumerate(data):
        for i in range(0,len(item)):
            if idx == 0 and i == 0:
                if item[i] < item[i+1] and item[i] < data[idx+1][i]:
                    small_numbers.append(int(item[i]))
            elif idx == 0 and i == len(item)-1:
                if item[i] < item[i-1] and item[i] < data[idx-1][i]:
                    small_numbers.append(int(item[i]))
            elif idx == len(data)-1 and i == 0:
                if item[i] < item[i+1] and item[i] < data[idx-1][i]:
                 small_numbers.append(int(item[i]))
            elif idx == len(data)-1 and i == len(item)-1:
                if item[i] < item[i-1] and item[i] < data[idx-1][i]:
                    small_numbers.append(int(item[i]))
            elif i == 0 and idx != 0 and idx != len(data)-1:
                if item[i] < item[i+1] and item[i] < data[idx-1][i] and item[i] < data[idx+1][i]:
                    small_numbers.append(int(item[i]))
            elif i == len(item)-1 and idx != 0 and idx != len(data)-1:
                if item[i] < item[i-1] and item[i] < data[idx-1][i] and item[i] < data[idx+1][i]:
                    small_numbers.append(int(item[i]))
            elif idx == 0 and i != 0 and i != len(item)-1:
                if item[i] < item[i+1] and item[i] < item[i-1] and item[i] < data[idx+1][i]:
                    small_numbers.append(int(item[i]))
            elif idx == len(data)-1 and i != 0 and i != len(item)-1:
                if item[i] < item[i+1] and item[i] < item[i-1] and item[i] < data[idx-1][i]:
                    small_numbers.append(int(item[i]))
            elif idx != 0 and idx != len(data)-1 and i != 0 and i != len(item)-1:
                if item[i] < item[i+1] and item[i] < item[i-1] and item[i] < data[idx-1][i] and item[i] < data[idx+1][i]:
                    small_numbers.append(int(item[i]))

    small_numbers = [x+1 for x in small_numbers]
    return sum(small_numbers)           


def parse(content):
    w = content.find('\n') + 1
    return list(map(int, content.replace('\n', '9') + w * '9')), w

def visit(heights, w, i, visited):
    visited.add(i)
    return 1 + sum(visit(heights, w, nb, visited)
                   for nb in (i - 1, i + 1, i - w, i + w)
                   if heights[nb] < 9 and nb not in visited)





print(smoke_detection(data))

heights, w = parse(data)
low = [i for i, height in enumerate(heights)
       if all(height < heights[nb] for nb in (i - 1, i + 1, i - w, i + w))]
print(sum(heights[i] + 1 for i in low))

a, b, c = sorted(visit(heights, w, i, set()) for i in low)[-3:]
print(a * b * c)


data = test_data.split('\n')
data.remove('')