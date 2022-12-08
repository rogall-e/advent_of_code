import math

with open('2022/input_files/day8.txt') as f:
    lines = f.read()

def get_data(data):    
    data = data.split('\n')
    return data

data = get_data(lines)

def counting_trees(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line.strip()):
            grid[x, y] = int(c)
            
    directions = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0),
    ]

    visibles_trees = set()
    scenic_scores = {}
    for tree in grid:
        scores = []
        for dx, dy in directions:
            x, y = tree
            score = 0
            while (x, y) in grid:
                nx = x + dx
                ny = y + dy

                if (nx, ny) not in grid:
                    visibles_trees.add(tree)
                    break
                elif grid[nx, ny] >= grid[tree]:
                    score += 1
                    break
                x = nx
                y = ny
                score += 1
            scores.append(score)
        scenic_scores[tree] = math.prod(scores)
    return len(visibles_trees), max(scenic_scores.values())

visibles_trees, scenic_scores=counting_trees(data)

print('part1: ', visibles_trees)
print('part2: ', scenic_scores)