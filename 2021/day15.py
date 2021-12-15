import numpy as np
from queue import PriorityQueue

with open('data/day15.txt') as f:
    data_input = f.read()
    
test_data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

def get_input(data):
    data = data.split('\n')
    data = [x.strip() for x in data if x]
    width = len(data[0])
    length = len(data)
    data = [int(y) for x in data for y in x]
    data = np.array(data).reshape(length, width)
    length = len(data)
    return data, length
    
def get_real_layout(data_array, new_array, length, repeats=0):
    if repeats == 0:
        new_array = data_array.copy()
        new_array += 1
        for x, y in zip(np.where(new_array > 9)[0], np.where(new_array > 9)[1]):
            new_array[x, y] = 1
        data_array = np.append(data_array, new_array, axis=1)
        repeats += 1
    while repeats <= 3:
        new_array += 1
        for x, y in zip(np.where(new_array > 9)[0], np.where(new_array > 9)[1]):
            new_array[x, y] = 1
        data_array = np.append(data_array, new_array, axis=1)
        repeats += 1
    if repeats == 4:
        new_array = data_array.copy()
        new_array += 1
        for x, y in zip(np.where(new_array > 9)[0], np.where(new_array > 9)[1]):
            new_array[x, y] = 1
        data_array = np.append(data_array, new_array, axis=0)
        repeats += 1
    while repeats <= 7:
        new_array += 1
        for x, y in zip(np.where(new_array > 9)[0], np.where(new_array > 9)[1]):
            new_array[x, y] = 1
        data_array = np.append(data_array, new_array, axis=0)
        repeats += 1      
    if repeats == 8:
        return data_array
    get_real_layout(data_array, new_array,length, repeats=repeats)
    
    
def calculate_way(data, part2=False):
    if part2:
        data, length = get_input(data)
        data = get_real_layout(data, np.array([]), length)
    else:
        data, length = get_input(data)

    data = np.pad(data, ((1,1), (1,1)), 'constant', constant_values=-1)
    start_point = (1, 1)
    end_point = (data.shape[0]-2, data.shape[1]-2)
    way_points = PriorityQueue()
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = set(start_point)
    way_points.put((0, start_point))
    way_point_dict = dict()
    
    while not way_points.empty():
        weight, point = way_points.get()
        for direction in DIRECTIONS:
            if data[direction[0] + point[0], direction[1] + point[1]] == -1:
                continue
            if (point[0] + direction[0], point[1] + direction[1]) not in visited:
                new_weight = weight + data[direction[0] + point[0], direction[1] + point[1]]
                way_points.put((new_weight, (point[0] + direction[0], point[1] + direction[1])))
                way_point_dict[(point[0] + direction[0], point[1] + direction[1])] = (new_weight)
                visited.add((point[0] + direction[0], point[1] + direction[1]))
            if (point[0] + direction[0], point[1] + direction[1]) == end_point:
                return way_point_dict[end_point]
                
               
           
print("part1:",calculate_way(data_input))
print("part2:",calculate_way(data_input, part2=True))