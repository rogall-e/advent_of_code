with open("data/day2.txt") as f:
    data = f.read()   
    
data = data.split("\n")
data.remove('')

def get_position(data):
    forward = 0
    aim = 0
    depth = 0
    for item in data:
        if item.startswith("forward"):
            forward += int(item.split(" ")[1])
            depth += (int(item.split(" ")[1]) * aim)
        elif item.startswith("up"):
            aim -= int(item.split(" ")[1])
        elif item.startswith("down"):
            aim += int(item.split(" ")[1])

    print(forward * depth)

get_position(data)