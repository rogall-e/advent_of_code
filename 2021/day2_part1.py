with open("data/day2.txt") as f:
    data = f.read()   
    
data = data.split("\n")
data.remove('')

def get_position(data):
    forward = 0
    down = 0
    up = 0
    for item in data:
        if item.startswith("forward"):
            forward += int(item.split(" ")[1])
        elif item.startswith("up"):
            up += int(item.split(" ")[1])
        elif item.startswith("down"):
            down += int(item.split(" ")[1])

    print(forward * (down - up))

get_position(data)