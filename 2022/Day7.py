from collections import defaultdict

with open('2022/input_files/day7.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    return data

data = get_data(lines)

def parse_file_system(data):
    filesystem_dict = defaultdict(int)
    processed_files = defaultdict(set)
    processing = False
    path = []
    for line in data:
        match line.split():
            case ["$", "cd", dirname]:
                processing = False
                match dirname:
                    case "..":
                        path.pop()
                    case "/":
                        path = ["/"]
                    case _:
                        path.append(dirname)
            case ["$", "ls"]:
                processing = True
            case [a, b]:
                if a.isnumeric():
                    if not processing or b in processed_files[tuple(path)]:
                        continue
                    processed_files[tuple(path)].add(b)
                    file_size = int(a)
                    for i in range(len(path)):
                        filesystem_dict[tuple(path[: i + 1])] += file_size
    return filesystem_dict

def part_1(data):
    filesystem_dict = parse_file_system(data)
    value_lst = []
    for value in filesystem_dict.values():
        if value <= 100000:
            value_lst.append(value)        
    return sum(value_lst)

def part_2(data):
    filesystem_dict = parse_file_system(data)
    sort_orders = sorted(filesystem_dict.items(), key=lambda x: x[1], reverse=True)
    directory_delete = []
    free_space = 70000000 - filesystem_dict[('/',)]
    for value in sort_orders:
        if value[1] >= 30000000-free_space:
            directory_delete.append(value[1])
    return directory_delete[-1]

print(part_1(data))
print(part_2(data))