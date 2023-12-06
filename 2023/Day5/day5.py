def day_five(data, part):
    seeds = [int(x) for x in data[0].split(": ")[1].split()]

    if part == "part_1":
        min_seed = get_min_seed(seeds, data)
        return min_seed


def get_min_seed(seeds, data):
    idx = 2
    for _ in range(len(data)):
        ranges_lst = []
        for line in data[idx + 1 :]:
            if line[:1].isdigit():
                ranges = [int(x) for x in line.split()]
                ranges = (
                    range(ranges[0], ranges[0] + ranges[2]),
                    range(ranges[1], ranges[1] + ranges[2]),
                )
                ranges_lst.append(ranges)

                idx += 1
            else:
                break
        idx += 1
        seeds = [check_mapping(seed, ranges_lst) for seed in seeds]
    return min(seeds)


def check_mapping(seed, ranges):
    for destination, source in ranges:
        if seed in source:
            return destination.start + seed - source.start
    return seed


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]
        print(day_five(data, "part_1"))
        # print(day_five(data, "part_2"))
