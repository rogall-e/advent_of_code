import random

with open("data/day12.txt") as f:
    data_final = f.read()


test_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

test_data_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""


def get_data(data):    
    data = data.split('\n')
    data.remove('')
    return data


def get_connections(data):
    data = get_data(data)
    connection_dict = {}
    for line in data:
        item_1 , item_2 = line.split('-')
        if item_1 in connection_dict and item_2 != 'start':
            connection_dict[item_1].append(item_2)
        elif item_1 not in connection_dict and item_2 != 'start':
            connection_dict[item_1] = [item_2]
        if item_2 in connection_dict and item_1 != 'start':
            connection_dict[item_2].append(item_1)
        elif item_2 not in connection_dict and item_1 != 'start':
            connection_dict[item_2] = [item_1]
    return connection_dict



def find_connections(last_point, seen_points, connection_dict, repeats):
    if last_point == 'end':
        return 1
    connections = 0
    for connection in connection_dict[last_point]:
        if not (connection.islower() and connection in seen_points):
            connections += find_connections(connection, seen_points | {last_point}, connection_dict, repeats)
        elif  connection.islower() and connection in seen_points and repeats:
            connections += find_connections(connection, seen_points | {last_point}, connection_dict, False)
    return connections
       
       
print(find_connections('start', set(), get_connections(data_final), False))
print(find_connections('start', set(), get_connections(data_final), True))

    
            

