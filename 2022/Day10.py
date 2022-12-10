with open('2022/input_files/day10.txt') as f:
    lines = f.read()

test_start = '''noop
addx 3
addx -5'''

def get_data(data):    
    data = data.split('\n')
    return data

data = get_data(lines)
data.append('noop')

def tick(no_cycles, counter, x, signal_strength):
    if counter in no_cycles:
        signal_strength.append(counter * x)
    return signal_strength

def part_1(data_input):
    X = 1
    addx = 0
    counter = 1
    cycles = [20,60,100,140,180,220]
    signal_strength = []

    for item in data:
        if item == "noop":
            counter += 1
        if item.startswith('addx'):
            item = item.replace('addx ', '')
            counter += 1
            signal_strength= tick(cycles, counter, X, signal_strength)
            counter += 1
            addx = int(item)
            X += addx
        signal_strength = tick(cycles, counter, X, signal_strength)        
    
    return sum(signal_strength)

 

def update_crt(counter, x, cycles, crt):
    sprite = [x-1,x,x+1]
    t1 = counter -1
    if counter < 40 and t1 in sprite:
        crt[0][t1] = '#'
    if counter < 80 and t1-40 in sprite:
        crt[1][t1-40] = '#'
    if counter < 120 and t1-80 in sprite:
        crt[2][t1-80] = '#'
    if counter < 160 and t1-120 in sprite:
        crt[3][t1-120] = '#'
    if counter < 200 and t1-160 in sprite:
        crt[4][t1-160] = '#'    
    if counter < 240 and t1-200 in sprite:
        crt[5][t1-200] = '#'   
    return crt

def part_2(data_input):
    X = 1
    addx = 0
    counter = 1
    cycles = [20,60,100,140,180,220]
    CRT = [[' ' for _ in range(40)] for _ in range(6)]
    for item in data:
        if item == "noop":     
            counter += 1
        if item.startswith('addx'):
            update_crt(counter, X, cycles, CRT)
            item = item.replace('addx ', '')
            counter += 1
            update_crt(counter, X, cycles, CRT)
            counter += 1
            addx = int(item)
            X += addx
        update_crt(counter, X, cycles, CRT)
    return CRT
    
    
print(part_1(data))
CRT = part_2(data)       
for _ in range(6):
        print(''.join(CRT[_]))
