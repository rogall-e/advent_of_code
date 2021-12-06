with open("data/day6.txt") as f:
    fish_age_start = f.readline()

fish_age_start = [int(x) for x in fish_age_start.split(',')]

fish_age = []
for item in fish_age_start:
    fish_age_dict = {
        'fish_age': item,
        'new_fish': False
    }
    fish_age.append(fish_age_dict)

def get_new_fish(fish_age, days, counter=0):
    counter
    for item in fish_age:
        item['fish_age'] -=  1
        if item['new_fish'] == True:
            fish_age_dict = {
                'fish_age': 9,
                'new_fish': False
            }
            fish_age.append(fish_age_dict)
        if item['fish_age'] == 0:
            item['new_fish'] = True
        if item['fish_age'] == -1:  
            item['fish_age'] = 6
            item['new_fish'] = False 
    if days == 0:
        return len(fish_age)
    else:
        return get_new_fish(fish_age, days-1, counter + 1)
        

def get_new_fish_2(fish_age, days):
    age_count = list(map(lambda n: fish_age.count(n), range(9)))
    for day in range(days):
        new_age_count = [0] * 9
        for i in range(8):
            new_age_count[i] = age_count[i+1]
        new_age_count[6] += age_count[0]
        new_age_count[8] = age_count[0]
        age_count = new_age_count
    return sum(age_count)


print(get_new_fish(fish_age, 79))
print(get_new_fish_2(fish_age_start, 256))
