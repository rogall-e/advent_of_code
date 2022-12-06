with open('2022/input_files/day6.txt') as f:
    lines = f.read()



def part_1(lines):
    reading_frame = []
    solution = 0
    for idx,item in enumerate(lines):
        reading_frame.append(item)
        if len(reading_frame) == 4:
            if len(set(reading_frame)) == 4:
                print(reading_frame)
                solution = idx +1
                break
            else:
                print(reading_frame)
                reading_frame.pop(0)
    return solution      

def part_2(lines):
    reading_frame = []
    solution = 0
    for idx,item in enumerate(lines):
        reading_frame.append(item)
        if len(reading_frame) == 14:
            if len(set(reading_frame)) == 14:
                print(reading_frame)
                solution = idx +1
                break
            else:
                print(reading_frame)
                reading_frame.pop(0)
    return solution  

print(part_1(lines))
print(part_2(lines))
    