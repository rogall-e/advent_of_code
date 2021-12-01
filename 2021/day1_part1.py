with open("data/day1.txt") as f:
    data = f.read()
    
data = data.split("\n")
data.remove('')
data = [int(x) for x in data]

print(len([item for idx, item in enumerate(data) if item > data[idx-1]]))