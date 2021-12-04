import numpy as np  # import numpy

with open("data/day4.txt") as f:
    drawing_numbers = f.readline()
    board_lst = []
    board_line = []
    counter = 0

    for line in f:
        if line != '\n':
            board_line.append(line.strip())  
        if len(board_line) == 5:
            board_lst.append(board_line)
            board_line = []
            
drawing_numbers = drawing_numbers.strip().split(',')


def create_board(board_lst):
    board_array = []
    for item in board_lst:
        board = [x for x in item.split(' ') if x.strip() != '']
        board_array.append(board)
    board_array = np.array(board_array)
    board_array = board_array.astype(float)
    return board_array

def check_winning(board_lst, number_lst):
    boards = board_lst
    winning_boards = []
    for idx, item in enumerate(boards):
        winning_condition = {
        'Answer': 0,
        'counter': len(board_lst)
        }  
        counter = 0
        board = create_board(item)
        for number in number_lst:
            number = float(number) 
            counter += 1
            if number in board:
                result = np.where(board == number)
                board[int(result[0])][int(result[1])] = np.nan
            if np.all(np.isnan(board), axis=1).any() or np.all(np.isnan(board), axis=0).any():
                if counter < len(board_lst) and np.all(np.isnan(board)) == False:
                    boards.remove(item)
                    winning_condition['counter'] = counter
                    winning_condition['Answer'] = number * np.nansum(board)
                    winning_boards.append(winning_condition)
                    break
                
    _lst = [x['counter'] for x in winning_boards]            
    for w in winning_boards:
        if w['counter'] == max(_lst):
            print(w['Answer'])
   
check_winning(board_lst, drawing_numbers)