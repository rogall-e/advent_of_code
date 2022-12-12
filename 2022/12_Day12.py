import numpy as np
from collections import deque
import string

with open('2022/input_files/day12.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    data = [x.strip() for x in data]
    return data

data = get_data(lines)

def string_to_array(data_input):
    low_alphabet = list(string.ascii_lowercase)
    hight_dict = dict()
    for idx,item in enumerate(low_alphabet):
        hight_dict[item] = idx + 1
    hight_dict['-'] = -1
    data = [list(x) for x in data_input]
    area_map = np.array(data)
    area_map = np.pad(area_map, ((1,1), (1,1)), 'constant', constant_values=-1)
    start_point = tuple()
    end_point = tuple()
    for (x,y), item in np.ndenumerate(area_map):
        if item == 'S':
            start_point = (x,y)
            area_map[x][y] = 'a'
        if item == 'E':
            end_point = (x,y)
            area_map[x][y] = 'z'    
    area_map = np.vectorize(hight_dict.get)(area_map)     
    return area_map, start_point, end_point

def get_connections(array_input):
    DIRECTIONS = [(1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')]
    connection_dict = {}
    for (x,y), item in np.ndenumerate(array_input):
        if item != -1:
            connection_dict[(x,y)] = []
        for direction in DIRECTIONS:
            if item != -1 and array_input[direction[0] + x, direction[1] + y] != -1 and\
                array_input[direction[0] + x, direction[1] + y]-item <= 1:
                connection_dict[(x,y)].append((direction[2],(direction[0] + x, direction[1] + y)))
    return connection_dict




def part_1(data_input):
    area_map, start_point, end_point = string_to_array(data_input)
    start, goal = start_point, end_point
    queue = deque([("", start)])
    visited = set()
    graph = get_connections(area_map)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
        
def part_2(data_input):
    area_map, start_point, end_point = string_to_array(data_input)
    way_up_hill = []
    for (x,y), item in np.ndenumerate(area_map):
        if item == 1:
            start_point = (x,y)
        start, goal = start_point, end_point
        queue = deque([("", start)])
        visited = set()
        graph = get_connections(area_map)
        while queue:
            path, current = queue.popleft()
            if way_up_hill != [] and len(path) >= min(way_up_hill):
                continue
            if current == goal:
                way_up_hill.append(len(path))
            if current in visited:
                continue
            visited.add(current)
            for direction, neighbour in graph[current]:
                queue.append((path + direction, neighbour))
        
    return min(way_up_hill)


print(len(part_1(data)))
print(part_2(data))
