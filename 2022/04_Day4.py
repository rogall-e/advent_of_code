with open('2022/input_files/day4.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    data = [x.replace('-', ',').split(',') for x in data]
    return data

data = get_data(lines)


def count_contain(data):
    counter = 0
    for item in data:
        if set(range(int(item[0]), int(item[1])+1)).issubset(range(int(item[2]), int(item[3])+1))\
            or set(range(int(item[2]), int(item[3])+1)).issubset(range(int(item[0]), int(item[1])+1)):
            counter += 1
    return counter

def count_overlap(data):
    counter = 0
    for item in data:
        if any(i in range(int(item[0]), int(item[1])+1) for i in range(int(item[2]), int(item[3])+1)):
            counter += 1
    return counter

print(count_contain(data))
print(count_overlap(data))

