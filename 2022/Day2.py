with open('2022/input_files/day2.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    return data

r_p_s = [x.split(' ') for x in get_data(lines)]

def calc_points_1(rps_data):
    play_dict = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors',
        'Y': 'Paper',
        'X': 'Rock',
        'Z': 'Scissors'
    }

    points_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    w_lst = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
    
    score = 0
    
    for item in rps_data:
        score += points_dict[item[1]]
        if item in w_lst:
            score += 6
        elif play_dict[item[0]] == play_dict[item[1]]:
            score += 3
            
    return score


def calc_points_2(rps_data):
    draw_dict = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    
    win_dict =  {
        'A': 2,
        'B': 3,
        'C': 1
    }
    
    loose_dict= {
        'A': 3,
        'B': 1,
        'C': 2
    }
    
    score = 0

    for item in rps_data:
        if item[1] == 'X':
            score += loose_dict[item[0]]
        elif item[1] == 'Y':
            score += 3
            score += draw_dict[item[0]]
        elif item[1] == 'Z':
            score += 6
            score += win_dict[item[0]]
            
    return score


print(calc_points_1(r_p_s))

print(calc_points_2(r_p_s))