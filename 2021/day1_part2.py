with open("data/day1.txt") as f:
    data = f.read()   
    
data = data.split("\n")
data.remove('')
data = [int(x) for x in data]

data_agg = [sum(data[i:i+3]) for i in range(len(data))] 
print(len([item for idx, item in enumerate(data_agg) if item > data_agg[idx-1]]))
