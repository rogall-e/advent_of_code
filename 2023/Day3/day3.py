from collections import defaultdict


def day_three(data, part):
    solution = 0
    width = len(data[0])
    height = len(data)

    star_dict = defaultdict(list)

    for idx, line in enumerate(data):
        x = 0
        while x < width:
            if not data[idx][x].isdigit():
                x += 1
                continue

            neighbors = check_neighbors(x, idx, width, height)

            digit = data[idx][x]

            for i in range(x + 1, width):
                if not data[idx][i].isdigit():
                    break

                digit += data[idx][i]
                neighbors.extend(check_neighbors(i, idx, width, height))
                x += 1
            if part == "part_1":
                if any(
                    data[ny][nx] != "." and not data[ny][nx].isdigit()
                    for nx, ny in neighbors
                ):
                    solution += int(digit)

                x += 1

            if part == "part_2":
                for nx, ny in neighbors:
                    if data[ny][nx] == "*":
                        star_dict[(nx, ny)].append(int(digit))
                        break
                x += 1

    if part == "part_2":
        for digits in star_dict.values():
            if len(digits) > 1:
                multiplication_result = 1
                for _ in digits:
                    multiplication_result *= _

                solution += multiplication_result

    return solution


def check_neighbors(x, y, width, height):
    neighbor_grid = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue

            nx = x + dx
            ny = y + dy

            if nx >= 0 and nx < width and ny >= 0 and ny < height:
                neighbor_grid.append((nx, ny))
    return neighbor_grid


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]
        print(day_three(data, "part_1"))
        print(day_three(data, "part_2"))
