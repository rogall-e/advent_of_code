with open('2022/input_files/day1.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    #data.remove('')
    return data

data = get_data(lines)
temp_lst = []
result = []
data.append('')


for idx, i in enumerate(data):
    if i != '':
        temp_lst.append(int(i))
    else:
        result.append(sum(temp_lst))
        temp_lst = []

result = sorted(result, reverse=True)
print(sum(result[:3]))
