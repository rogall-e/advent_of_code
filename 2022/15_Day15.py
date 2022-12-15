from parse import *
from parse import compile
from scipy.spatial.distance import cityblock
from tqdm import tqdm
import numpy as np

with open('2022/input_files/day15.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    return data

test_data='''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''


data = get_data(lines)


def preprocess_data(data_input):
    sb = compile('Sensor at x={}, y={}: closest beacon is at x={}, y={}')
    min_depth =0
    min_width =0
    max_width = 0
    max_depth = 0
    sensors = []
    beacons = []

    for idx,line in enumerate(data):
        xs,ys,xb,yb = sb.parse(line)
        sensors.append((int(xs),int(ys)))
        beacons.append((int(xb),int(yb)))
        if min(int(xb),int(xs)) < min_width:
            min_width = min(int(xb),int(xs))
        if min(int(yb),int(ys)) < min_depth:
            min_depth = min(int(yb),int(ys))
        if max(int(xb),int(xs)) > max_width:
            max_width = max(int(xb),int(xs))
        if max(int(yb),int(ys)) > max_depth:
            max_depth = max(int(yb),int(ys))
    return sensors,beacons, max_depth, max_width, min_depth, min_width
        
def part_1(data_input, row):
    sensors,beacons, max_depth, max_width, min_depth, min_width = preprocess_data(data_input)
    row_lst = [(x,row) for x in range(min_width-row, max_width+row)]
    impossible_points = set()
    for sensor, beacon in zip(sensors,beacons):
        manhattan = cityblock([sensor[0],sensor[1]], [beacon[0],beacon[1]])
        for i in tqdm(range(len(row_lst))):
            point = (row_lst[i][0],row_lst[i][1])
            manhattan_distance_row = cityblock([sensor[0],sensor[1]], [point[0],point[1]])
            if manhattan_distance_row <= manhattan and point != beacon:
                impossible_points.add(point)
    return len(impossible_points)

def part_2(data_input,w_h):
    print('still running_1')
    sensors,beacons, max_depth, max_width, min_depth, min_width = preprocess_data(data_input)
    grid = np.full((w_h,w_h),'.')
    for sensor, beacon in zip(sensors,beacons):
        manhattan = cityblock([sensor[0],sensor[1]], [beacon[0],beacon[1]])
        print('still running')
        for (x,y), item in np.ndenumerate(grid):
            point = (x,y)
            manhattan_distance_row = cityblock([sensor[0],sensor[1]], [point[0],point[1]])
            if manhattan_distance_row <= manhattan:
                grid[x,y] = '#'
    x,y = np.where(grid == '.')
    return (x*4000000)+y


print(part_2(data,4000000))
    