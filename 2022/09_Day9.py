import math
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

with open('2022/input_files/day9.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    return data

data = get_data(lines)
moves = [x.split(" ") for x in data]

moves_test = [['R',5],['U', 8],['L', 8],['D', 3],['R', 17],['D', 10],['L', 25],['U', 20]]


def check_neighbors(hx, hy, k, T):
    if k=='R':
        T = [hx,hy-1]
    elif k=='L':
        T = [hx,hy+1]
    elif k=='U':
        T = [hx-1,hy]
    elif k=='D':
        T = [hx+1,hy]
    return T


def tail_position(t):
    T_moves_new = []
    T_new = [0,0]
    for idx,(tx_prev,ty_prev) in enumerate(t):
        if abs(math.dist(T_new,[tx_prev,ty_prev]))==1 or abs(math.dist(T_new,[tx_prev,ty_prev]))==math.dist([0,0],[1,1]) or\
            math.dist(T_new,[tx_prev,ty_prev])==0:
            tx = T_new[0]
            ty = T_new[1]
            T_moves_new.append((tx,ty))
            continue
        else:
            if t[idx-1][1] < t[idx][1]:
                k="R"
            if t[idx-1][1] > t[idx][1]:
                k="L"
            if t[idx-1][0] < t[idx][0]:
                k="U"
            if t[idx-1][0] > t[idx][0]:
                k="D"
            T_new = check_neighbors(tx_prev,ty_prev,k,T_new)
            tx = T_new[0]
            ty = T_new[1]
            T_moves_new.append((tx,ty))
    return T_moves_new


def part_1(move_input):
    directions = {
    'R' : [0, 1],
    'L' : [0, -1],
    'U' : [1, 0],
    'D' : [-1, 0]
    }

    H = [0,0]
    T = [0,0]

    H_moves = []
    T_moves = []
    for k,v in move_input: 
        for _ in range(int(v)):
            H[0] = H[0] + directions[k][0]
            H[1] = H[1] + directions[k][1]
            hx = H[0]
            hy = H[1]
            H_moves.append((hx,hy))
            if abs(math.dist(T,[hx,hy]))==1 or abs(math.dist(T,[hx,hy]))==math.dist([0,0],[1,1]) or\
                math.dist(T,[hx,hy])==0:
                tx = T[0]
                ty = T[1]
                T_moves.append((tx,ty))
                continue
            else:
                T = check_neighbors(hx,hy,k,T)
                tx = T[0]
                ty = T[1]
                T_moves.append((tx,ty))
    return  len(set(T_moves))  
            
           
#Doesn't work!
def part_2(move_input):
    directions = {
        'R' : [0, 1],
        'L' : [0, -1],
        'U' : [1, 0],
        'D' : [-1, 0]
        }

    H = [0,0]
    T_1 = [0,0]

    H_moves = []
    T_moves = []
    
    for k,v in move_input: 
        for _ in range(int(v)):
            H[0] = H[0] + directions[k][0]
            H[1] = H[1] + directions[k][1]
            hx = H[0]
            hy = H[1]
            H_moves.append((hx,hy))
            if abs(math.dist(T_1,[hx,hy]))==1 or abs(math.dist(T_1,[hx,hy]))==math.dist([0,0],[1,1]) or\
                math.dist(T_1,[hx,hy])==0:
                tx = T_1[0]
                ty = T_1[1]
                T_moves.append((tx,ty))
                continue
            else:
                T_1 = check_neighbors(hx,hy,k,T_1)
                tx = T_1[0]
                ty = T_1[1]
                T_moves.append((tx,ty))
    
    for _ in range(9):
        print(len(set(T_moves)))
        T_moves_new = tail_position(T_moves)
        T_moves = T_moves_new
    
    return len(set(T_moves))     
        
    

print('T:', part_2(moves_test))
print('T:', part_1(moves_test))

