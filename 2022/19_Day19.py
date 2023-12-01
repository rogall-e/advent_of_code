from parse import compile, parse
from collections import defaultdict

with open('2022/input_files/day15.txt') as f:
    lines = f.read()

def get_data(data):
    data = data.split('\n')
    return data

test_data = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
'''
data = get_data(test_data)

def get_blueprint(data_input):
    data = get_data(test_data)
    data = [x.split('. ') for x in data]
    blueprints = defaultdict(dict)
    ore_robot = compile('Blueprint {}: Each ore robot costs {} ore')
    clay_robot = compile('Each clay robot costs {} ore')
    obsidian_robot = compile('Each obsidian robot costs {} ore and {} clay')
    geode_robot = compile('Each geode robot costs {} ore and {} obsidian.')
    for blueprints_lst in data:
        for blueprint in blueprints_lst:
            if blueprint.startswith('Blueprint '):
                ore_robot_cost = ore_robot.parse(blueprint)
            if blueprint.startswith('Each clay'):   
                clay_robot_cost = clay_robot.parse(blueprint)
            if blueprint.startswith('Each obsidian'):   
                obsidian_robot_cost = obsidian_robot.parse(blueprint)
            if blueprint.startswith('Each geode'):    
                geode_robot_cost = geode_robot.parse(blueprint)
        robots_cost = {
            'ore': [int(ore_robot_cost[1]),0,0],
            'clay':[int(clay_robot_cost[0]),0,0],
            'obsidian':[int(obsidian_robot_cost[0]),int(obsidian_robot_cost[1]),0],
            'geode':[int(geode_robot_cost[0]),0,int(geode_robot_cost[1])]
        }
        blueprints[f'blueprint_{ore_robot_cost[0]}'] = robots_cost
    return blueprints
  
def find_max_geode(data_input):
    max_geodes = 0
    blueprints = get_blueprint(data_input)
    for blueprint in blueprints.values():
        ore = 0
        clay = 0
        obsidian = 0
        geode = 0
        robots = {
            'ore': 1,
            'clay':0,
            'obsidian':0,
            'geode':0
        }
        for i in range(1,25):
            print('-----'*5)
            print('Round:', i)
            print('At Start: Ore:', ore, '| Clay:', clay,'| Obsidian:', obsidian,'| Geode:', geode)
            if ore >= blueprint['ore'][0]:# and\
                #(clay <= blueprint['obsidian'][1]//2 and\
                #obsidian <= blueprint['geode'][2]//2):
                robots['ore'] += 1
                ore -= blueprint['ore'][0]
                ore -= 1
                print('Build ore robot!')
            if ore >= blueprint['clay'][0]: #and\
                #(clay <= blueprint['obsidian'][1]//2 and\
                #obsidian <= blueprint['geode'][2]//2):
                robots['clay'] += 1
                ore -= blueprint['clay'][0]
                clay -= 1
                print('Build clay robot!')
            if ore >= blueprint['obsidian'][0] and\
                clay >= blueprint['obsidian'][1]:# and\
                #obsidian <= blueprint['geode'][2]:
                robots['obsidian'] += 1
                ore -= blueprint['obsidian'][0]
                clay -= blueprint['obsidian'][1]
                obsidian -= 1
                print('Build obsidian robot!')
            if ore >= blueprint['geode'][0] and\
                obsidian >= blueprint['geode'][2]:
                robots['geode'] += 1
                ore -= blueprint['geode'][0]
                obsidian -= blueprint['geode'][2]
                geode -= 1
                print('Build geode robot!')

            ore += robots['ore']    
            clay += robots['clay']    
            obsidian += robots['obsidian']    
            geode += robots['geode']
            print('At End: Ore:', ore, '| Clay:', clay,'| Obsidian:', obsidian,'| Geode:', geode)
            print(robots)
    # return max_geodes
    
find_max_geode(test_data)