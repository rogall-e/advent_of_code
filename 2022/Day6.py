with open('2022/input_files/day6.txt') as f:
    lines = f.read()



def solution(lines, codon=4):
    reading_frame = []
    solution = 0
    for idx,item in enumerate(lines):
        reading_frame.append(item)
        if len(reading_frame) == codon:
            if len(set(reading_frame)) == codon:
                solution = idx +1
                break
            else:
                reading_frame.pop(0)
    return solution      


print(solution(lines))
print(solution(lines, 14))
    