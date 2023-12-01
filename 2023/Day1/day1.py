# day 1 of aoc 2023


def day_one(data, part):
    digit_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    digit_lst = []
    for items in data:
        if len(items) > 0:
            digits_in_str = []
            if part == "part_1":
                digits_in_str = [i for i in items if i.isdigit()]
                digit_lst.append(digits_in_str)
            if part == "part_2":
                for i, c in enumerate(items):
                    for key, value in digit_dict.items():
                        if items[i:].startswith(key):
                            digits_in_str.append(digit_dict[key])
                    if c.isdigit():
                        digits_in_str.append(c)
                digit_lst.append(digits_in_str)
    solution_lst = []
    for digits in digit_lst:
        first_digit = digits[0]
        last_digit = digits[-1]

        digit = int(first_digit + last_digit)

        solution_lst.append(digit)

    return sum(solution_lst)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]
        print(day_one(data, "part_1"))
        print(day_one(data, "part_2"))
