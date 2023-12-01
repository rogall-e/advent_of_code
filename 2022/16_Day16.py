import networkx as nx
from parse import compile, parse
from collections import defaultdict

with open('2022/input_files/day15.txt') as f:
    lines = f.read()

def get_data(data):
    data = data.split('\n')
    return data

test_data = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''


data = get_data(test_data)


sb = compile('Valve {} has flow rate={}; tunnels lead to valves {}')
sb_single = compile('Valve {} has flow rate={}; tunnel leads to valve {}')

valves = []

for item in data:
    if 'to valves' in item:
        valve, flow_rate, to_valves = sb.parse(item)
    else:
        valve, flow_rate, to_valves = sb_single.parse(item)
    flow_rate = int(flow_rate)
    to_valves = [_.strip() for _ in to_valves.split(',')]
    valves.append([valve, flow_rate, to_valves])
    
G = nx.DiGraph()
flow_lst = []
for valve in valves:
    for direction in valve[2]:
        G.add_edge(valve[0],direction)
        flow_lst.append((valve[0],valve[1]))
      
#flow_lst.sort(key=lambda x: x[1], reverse=True)


valve_dict = {}
connection_dict = defaultdict(list)
for valve_1 in flow_lst:
    valve_dict[valve_1[0]] = valve_1[1]
    for valve_2 in flow_lst:
        steps = len(nx.shortest_path(G, source=valve_1[0], target=valve_2[0]))
        if (valve_2[0], steps) not in connection_dict[valve_1[0]]:
            connection_dict[valve_1[0]].append((valve_2[0], steps))

cycles = 31   
counter = 1
next_valve = 'AA'
pressure = 0
way=[]
visited = ['AA']
while cycles != 0:
    counter += 1
    pressure_gain_best = 0
    minutes = 30
    for valve2,steps in connection_dict[next_valve]:
        print(visited)
        if steps >= minutes and valve2 in visited:
            continue
        minutes -= steps 
        pressure_gain = valve_dict[valve2] * minutes
        if pressure_gain_best < pressure_gain:
            pressure_gain_best = pressure_gain
            visited.append(valve2)
            next_valve = valve2
            pressure += valve_dict[valve2]
    print(counter)    
    if counter % 2 == 0:
        visited.pop(0)
    cycles -= steps
    print(f'Next Valves: {next_valve}')
    print("Pressure: ", pressure)
    print("Minutes: ", minutes) 
    print("Steps: ", steps) 
    way.append(next_valve)
    
print(way)

