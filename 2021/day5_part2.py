from collections import Counter
with open("data/day5.txt") as f:
    data = f.read()

test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

data = data.split("\n")
data.remove('')
data = [x.split(' -> ') for x in data]

def get_borders(data):
    ver_and_hori = []
    diagonals = []
    for border in data:
        x1,y1 = border[0].split(',')
        x2,y2 = border[1].split(',')
        if x1 == x2:
            if int(y1) < int(y2):
                for i in range(int(y1), int(y2)+1):
                    ver_and_hori.append((int(x1),i))
            else:
                for i in range(int(y1), int(y2)-1, -1):
                    ver_and_hori.append((int(x1),i))
        elif y1 == y2:
            if int(x1) < int(x2):
                for i in range(int(x1), int(x2)+1):
                    ver_and_hori.append((i,int(y1)))
            else:
                for i in range(int(x1), int(x2)-1, -1):
                    ver_and_hori.append((i,int(y1)))
        elif int(x1) != int(x2) and int(y1) != int(y2):
            if int(x1) < int(x2) and int(y1) < int(y2):
                for i, j in zip(range(int(x1), int(x2)+1), range(int(y1), int(y2)+1)):
                        diagonals.append((i,j))
            elif int(x1) < int(x2) and int(y1) > int(y2):
                for i, j in zip(range(int(x1), int(x2)+1), range(int(y1), int(y2)-1,-1)):
                        diagonals.append((i,j))
            elif int(x1) > int(x2) and int(y1) < int(y2):
                for i, j in zip(range(int(x1), int(x2)-1, -1),range(int(y1), int(y2)+1)):
                        diagonals.append((i,j))
            elif int(x1) > int(x2) and int(y1) > int(y2):
                for i, j in zip(range(int(x1), int(x2)-1,-1),range(int(y1), int(y2)-1,-1)):
                        diagonals.append((i,j))
    borders = diagonals + ver_and_hori
    return borders


def count_overlap(data):
    min_threshold = 2
    borders = get_borders(data)
    counting_dict = Counter(borders)
    counting_dict_thrs = {x: count for x, count in counting_dict.items() if count >= min_threshold}
    return len(counting_dict_thrs)
            


print(count_overlap(data))