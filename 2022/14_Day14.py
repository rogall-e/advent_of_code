import numpy as np

with open('2022/input_files/day14.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    data = [x.split('->') for x in data]
    return data

test_data = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9'''


data = get_data(lines)
start_point = (500,0)

transform = lambda x,y: (int(x.strip()), int(y.strip()))

def get_rocks(data):
    rocks = set()
    for item in data:
        for i in range(len(item)-1):
            x1 = item[i][0]
            y1 = item[i][1]
            x2 = item[i+1][0]
            y2 = item[i+1][1]
            rocks.add((x1,y1))
            rocks.add((x2,y2))
            if x1 == x2:
                if y1 < y2:
                    for i in range(y1, y2+1):
                        rocks.add((x1,i))
                else:
                    for i in range(y1, y2-1, -1):
                        rocks.add((x1,i))
            elif y1 == y2:
                if x1 < x2:
                    for i in range(x1, x2+1):
                        rocks.add((i,y1))
                else:
                    for i in range(x1, x2-1, -1):
                        rocks.add((i,y1)) 
    return rocks

min_width = 0
max_width = 0
max_depth = 0

for item in data:
    for idx,rocks in enumerate(item):
        x,y = rocks.split(',')
        item[idx] = transform(x,y)
        min_width = int(x.strip())
        if int(x.strip()) < min_width:
            min_width = int(x.strip())
        if int(x.strip()) > max_width:
            max_width = int(x.strip())
        if int(y.strip()) > max_depth:
            max_depth = int(y.strip())
rocks = get_rocks(data)          

ground = get_rocks([[(0,max(rocks, key = lambda t: t[1])[1]+2),(750,max(rocks, key = lambda t: t[1])[1]+2)]])


def part_1(rocks):
    grid = np.full((751,172), '.')
    current_position = start_point
    sand = 0
    for rock in rocks:
        grid[rock[0],rock[1]] = '#'
    while True:
        x,y = current_position
        if y >= max(rocks, key = lambda t: t[1])[1]:
            break
        if grid[x,y+1] == '.':
            current_position = (x,y+1)
        elif grid[x-1,y+1] == '.':
            current_position = (x-1,y+1)
        elif grid[x+1,y+1] == '.':
            current_position = (x+1,y+1)
        elif grid[x,y+1] and grid[x-1,y+1] and grid[x+1,y+1] !='.': 
            sand += 1
            grid[x,y] = 'O'
            current_position = start_point  
    with open('2022/output/grid_after_1.txt','w') as f:  
        grid_out = np.rot90(grid,3)
        np.savetxt(f, grid_out, fmt='%s')
    return sand  
      

def part_2(rocks,ground, start_point):
    xs = start_point[0]
    ys = start_point[1]
    grid = np.full((751,173), '.')
    current_position = start_point
    sand = 0
    rocks = rocks | ground
    for rock in rocks:
        grid[rock[0],rock[1]] = '#'
    while True:
        x,y = current_position
        if grid[xs,ys] == 'O':
            break
        if grid[x,y+1] == '.':
            current_position = (x,y+1)
        elif grid[x-1,y+1] == '.':
            current_position = (x-1,y+1)
        elif grid[x+1,y+1] == '.':
            current_position = (x+1,y+1)
        elif grid[x,y+1] and grid[x-1,y+1] and grid[x+1,y+1] !='.': 
            sand += 1
            grid[x,y] = 'O'
            current_position = start_point
    with open('2022/output/grid_after_2.txt','w') as f:  
        grid_out = np.rot90(grid,3)
        np.savetxt(f, grid_out, fmt='%s')
    return sand  
   
print(part_1(rocks))
print(part_2(rocks,ground,start_point))
    

