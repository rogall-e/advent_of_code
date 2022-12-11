from collections import defaultdict
from parse import *
from math import lcm

with open('2022/input_files/day11.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    data = [x.strip() for x in data]
    return data

data = get_data(lines)



def parse_data(data_input):
    monkee_acticity = defaultdict()
    for idx,item in enumerate(data):
        if item.startswith('Monkey'):
            monkey_no = parse("Monkey {}:", item)[0]
            monkee_acticity[f'monkey_{monkey_no}'] = {}
            
            start_items = data[idx+1]
            start_items_value = parse("Starting items: {}", start_items)[0]
            monkee_acticity[f'monkey_{monkey_no}']['items'] = []
            monkee_acticity[f'monkey_{monkey_no}']['items'] = [int(x.strip()) for x in start_items_value.split(',')]
            
            operation = data[idx+2]
            operation = parse("Operation: new = old {}", operation)[0]
            operation = operation.split(' ')
            monkee_acticity[f'monkey_{monkey_no}']['operation'] = [operation[0], operation[1]]
            
            test = data[idx+3]
            test = parse("Test: divisible by {}", test)[0]
            monkee_acticity[f'monkey_{monkey_no}']['test'] = int(test)
            
            target_true = data[idx+4]
            target_true = parse("If true: throw to monkey {}", target_true)[0]
            monkee_acticity[f'monkey_{monkey_no}']['target_true'] = f'monkey_{target_true}'
            
            target_false = data[idx+5]
            target_false = parse("If false: throw to monkey {}", target_false)[0]
            monkee_acticity[f'monkey_{monkey_no}']['target_false'] = f'monkey_{target_false}'
            
            monkee_acticity[f'monkey_{monkey_no}']['inspected_items'] = 0
    return monkee_acticity

def get_answer(dict_input):
    inspected_items_lst = []           
    for k in dict_input.keys():
        i = dict_input[k]['inspected_items']
        inspected_items_lst.append(i)
    inspected_items_lst_sorted = sorted(inspected_items_lst, reverse=True)  
    answer = inspected_items_lst_sorted[0] * inspected_items_lst_sorted[1] 
    return answer

def part_1(data_input):
    monkee_acticity = parse_data(data_input)
    for i in range(20):
        for k,v in monkee_acticity.items():
            items_new = []
            if monkee_acticity[k]['operation'][1] == 'old':
                items_old = monkee_acticity[k]['items']
                items_new = [(x*x)//3 for x in items_old]
                monkee_acticity[k]['items'] = []
            elif monkee_acticity[k]['operation'][0] == '+':
                worry_increase = monkee_acticity[k]['operation'][1]
                items_old = monkee_acticity[k]['items']
                items_new = [(x+int(worry_increase))//3 for x in items_old]
                monkee_acticity[k]['items'] = [] 
            elif monkee_acticity[k]['operation'][0] == '*':
                worry_increase = monkee_acticity[k]['operation'][1]
                items_old = monkee_acticity[k]['items']
                items_new = [(x*int(worry_increase))//3 for x in items_old]
                monkee_acticity[k]['items'] = []    
            for _ in items_new:
                monkee_acticity[k]['inspected_items'] += 1
                if _ % monkee_acticity[k]['test'] == 0:
                    new_monkey = monkee_acticity[k]['target_true']
                    monkee_acticity[new_monkey]['items'].append(_)
                else: 
                    new_monkey = monkee_acticity[k]['target_false']
                    monkee_acticity[new_monkey]['items'].append(_)
    answer = get_answer(monkee_acticity)    
    return answer

def part_2(data_input):
    monkee_acticity = parse_data(data_input)
    tests = []
    for k,v in monkee_acticity.items():
        tests.append(monkee_acticity[k]['test'])
    modulo = lcm(*tests)
    for i in range(10000):
        for k,v in monkee_acticity.items():
            items_new = []
            if monkee_acticity[k]['operation'][1] == 'old':
                items_old = monkee_acticity[k]['items']
                items_new = [(x*x)%modulo for x in items_old]
                monkee_acticity[k]['items'] = []
            elif monkee_acticity[k]['operation'][0] == '+':
                worry_increase = monkee_acticity[k]['operation'][1]
                items_old = monkee_acticity[k]['items']
                items_new = [(x+int(worry_increase))%modulo for x in items_old]
                monkee_acticity[k]['items'] = [] 
            elif monkee_acticity[k]['operation'][0] == '*':
                worry_increase = monkee_acticity[k]['operation'][1]
                items_old = monkee_acticity[k]['items']
                items_new = [(x*int(worry_increase))%modulo for x in items_old]
                monkee_acticity[k]['items'] = []    
            for _ in items_new:
                monkee_acticity[k]['inspected_items'] += 1
                if _ % monkee_acticity[k]['test'] == 0:
                    new_monkey = monkee_acticity[k]['target_true']
                    monkee_acticity[new_monkey]['items'].append(_)
                else: 
                    new_monkey = monkee_acticity[k]['target_false']
                    monkee_acticity[new_monkey]['items'].append(_)
    inspected_items_lst = []           
    for k in monkee_acticity.keys():
        i = monkee_acticity[k]['inspected_items']
        inspected_items_lst.append((k,i))   
    answer = get_answer(monkee_acticity)    
    return answer

     
print(part_1(data))
print(part_2(data))
        
    
        



    