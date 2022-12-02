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

for i in data:
    if i != '':
        temp_lst.append(int(i))
    else:
        result.append(sum(temp_lst))
        temp_lst = []

result = sorted(result, reverse=True)
print('Answer question 1: ', result[0])
print('Answer question 2: ', sum(result[:3]))
