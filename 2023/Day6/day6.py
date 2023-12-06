from math import prod


def day_six(data, part):
    if part == "part_1":
        times = [int(x) for x in data[0].split() if x != "Time:"]
        distances = [int(x) for x in data[1].split() if x != "Distance:"]
        winning_distance_lst = []
        for idx, time in enumerate(times):
            winning_distances = 0
            for ms in range(time):
                if ms == 0:
                    continue
                distance_travelled = (time - ms) * ms
                if distance_travelled > distances[idx]:
                    winning_distances += 1

            winning_distance_lst.append(winning_distances)

        return prod(winning_distance_lst)
    if part == "part_2":
        times = [x for x in data[0].split() if x != "Time:"]
        distances = [x for x in data[1].split() if x != "Distance:"]

        time = int("".join(times))
        distance = int("".join(distances))
        winning_distances = 0
        for ms in range(time):
            if ms < 14:
                continue
            distance_travelled = (time - ms) * ms
            if distance_travelled > distance:
                winning_distances += 1

        return winning_distances


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]
        print(day_six(data, "part_1"))
        print(day_six(data, "part_2"))
