with open("data/day3.txt") as f:
    data = f.read()   
    
data = data.split("\n")
data.remove('')


def calc_power(data):
    l = len(data[0])
    gamma = ''
    epsilon = ''
    for i in range(0, l):
        counting_dict = {
                '1': 0,
                '0': 0
            }
        for item in data:
            if item[i] == '1':
                counting_dict['1'] += 1
            else:
                counting_dict['0'] += 1
        if counting_dict['1'] > counting_dict['0']:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma,2) * int(epsilon,2)
 
def calc_co2_o2(data):
    data_o2 = data.copy()
    data_co2 = data.copy()
    counter = 0
    while len(data_o2) > 1:
            counting_dict_02 = {
                '1': 0,
                '1_idx': [],
                '0': 0,
                '0_idx': []
            }
            for idx,item in enumerate(data_o2):
                if item[counter] == '1':
                    counting_dict_02['1'] += 1
                    counting_dict_02['1_idx'].append(idx)
                else:
                    counting_dict_02['0'] += 1
                    counting_dict_02['0_idx'].append(idx) 
            if counting_dict_02['1'] > counting_dict_02['0']:
                data_o2 = [j for idx_, j in enumerate(data_o2) if idx_ in counting_dict_02['1_idx']]
            elif counting_dict_02['1'] == counting_dict_02['0']:
                data_o2 = [j for idx_, j in enumerate(data_o2) if idx_ in counting_dict_02['1_idx']]
            else:
                data_o2 = [j for idx_, j in enumerate(data_o2) if idx_ in counting_dict_02['0_idx']]
            counter += 1    
    counter = 0          
    while len(data_co2) > 1:
            counting_dict_co2 = {
                '1': 0,
                '1_idx': [],
                '0': 0,
                '0_idx': []
            }
            for idx,item in enumerate(data_co2):
                if item[counter] == '1':
                    counting_dict_co2['1'] += 1
                    counting_dict_co2['1_idx'].append(idx)
                else:
                    counting_dict_co2['0'] += 1
                    counting_dict_co2['0_idx'].append(idx)   
            if counting_dict_co2['1'] > counting_dict_co2['0']:
                data_co2 = [j for idx_, j in enumerate(data_co2) if idx_ in counting_dict_co2['0_idx']]
            elif counting_dict_co2['1'] == counting_dict_co2['0']:
                data_co2 = [j for idx_, j in enumerate(data_co2) if idx_ in counting_dict_co2['0_idx']]
            elif counting_dict_co2['1'] < counting_dict_co2['0']:
                data_co2 = [j for idx_, j in enumerate(data_co2) if idx_ in counting_dict_co2['1_idx']]
            counter += 1
    
    return int(data_o2[0],2) * int(data_co2[0],2)

print('Power:', calc_power(data))

print('O2 and CO2:', calc_co2_o2(data))