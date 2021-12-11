import numpy as np

with open("data/day11.txt") as f:
    data = f.read()
    
test_data_1 = '''11111
19991
19191
19991
11111
'''

test_data_2 = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''

    
data = data.split('\n')
data.remove('')

print(data)
STEPS = 100


def add_border(data) -> np.array:
    border_lst = []
    for i in range(len(data[0])+2):
        border_lst.append(-1)

    data = [list(map(int, line)) for line in data]
    for item in data:
        item.insert(0, -1)
        item.append(-1)
    data.insert(0, border_lst)
    data.append(border_lst)


    data_array = np.array(data)
    return data_array

def creating_flashes(data_array,flashed, neighbors, step):
        new_flashed = set()
        for x in range(len(data_array)):
            for y in range(len(data_array[0])):
                if data_array[x][y] == -1:
                    data_array[x][y] == -1
                else:
                    if step == 0:
                        data_array[x][y] += 1
                        if data_array[x][y] > 9:
                            flashed.add((x,y))
                            data_array[x][y] = 0
                            new_flashed.add((x,y))
                    elif step > 0:
                        if data_array[x][y] > 9:
                            flashed.add((x,y))
                            data_array[x][y] = 0
                            new_flashed.add((x,y))
        if step == 0:             
            for (x,y) in flashed:
                for (dx,dy) in neighbors:
                    if data_array[x+dx][y+dy] == -1:
                        data_array[x+dx][y+dy] = -1
                    elif (x+dx, y+dy) not in flashed:
                        data_array[x+dx][y+dy] += 1
                    elif (x+dx, y+dy) not in flashed and data_array[x+dx][y+dy] > 9:
                        data_array[x+dx][y+dy] = 0
                        new_flashed.add((x+dx,y+dy))
                    elif (x+dx, y+dy) in flashed:
                        data_array[x+dx][y+dy] = 0
        elif step > 0:
            for (x,y) in new_flashed:
                for (dx,dy) in neighbors:
                    if data_array[x+dx][y+dy] == -1:
                        data_array[x+dx][y+dy] = -1
                    elif (x+dx, y+dy) not in flashed:
                        data_array[x+dx][y+dy] += 1
                    elif (x+dx, y+dy) not in flashed and data_array[x+dx][y+dy] > 9:
                        data_array[x+dx][y+dy] = 0
                        new_flashed.add((x+dx,y+dy))
                    elif (x+dx, y+dy) in flashed:
                        data_array[x+dx][y+dy] = 0                 
        
        return data_array
    
        
def squids_1(data, steps):
    data_array = add_border(data)
    neighbors = [(-1,-1),(-1,0),(-1,1), (0,-1), (1,-1), (1,0),(1,1), (0,1)]
    
    flashed = set()
    counting_flashes=0
    for i in range(0, STEPS):
        print('--------------------------------')
        print('STEP: ', i + 1)
        counter = 0
        data_array = creating_flashes(data_array,flashed, neighbors, counter)
        still_flashes = True
        while still_flashes:
            counter += 1
            if np.count_nonzero(data_array > 9) == 0:  
                still_flashes = False
            else:
                data_array = creating_flashes(data_array,flashed, neighbors, counter)

        print(f'After step {i}: \n', data_array)
                
        counting_flashes += len(flashed)
        flashed = set()
    return counting_flashes 
                        

def squids_2(data):
    data_array = add_border(data)
    neighbors = [(-1,-1),(-1,0),(-1,1), (0,-1), (1,-1), (1,0),(1,1), (0,1)]
    all_flashed = False
    flashed = set()
    counting_flashes=0
    counting_steps = 0
    while not all_flashed:
        counting_steps += 1
        print('--------------------------------')
        print('STEP: ', counting_steps)
        counter = 0
        data_array = creating_flashes(data_array,flashed, neighbors, counter)
        still_flashes = True
 
        while still_flashes:
            counter += 1
            if np.count_nonzero(data_array > 9) == 0:
                still_flashes = False
            else:
                data_array = creating_flashes(data_array,flashed, neighbors, counter)
        print(f'After step {counting_steps}: \n', data_array)
        counting_flashes += len(flashed)
        flashed = set()
        if np.count_nonzero(data_array == 0) == (len(data_array) - 2)**2:
            all_flashed = True
        
        
    return counting_steps 


print(squids_1(data, STEPS))
print(squids_2(data))


