# Advent of code day2
from parse import *
import re


def pattern_matching(iteration):
    blue_pattern = r"(\d+)\s+blue"
    red_pattern = r"(\d+)\s+red"
    green_pattern = r"(\d+)\s+green"

    match_blue = re.search(blue_pattern, iteration)
    match_red = re.search(red_pattern, iteration)
    match_green = re.search(green_pattern, iteration)
    return match_green, match_red, match_blue


def day_two(data, part):
    bag = {"red": 12, "green": 13, "blue": 14}

    if part == "part_1":
        sum_of_ids = 0
        for idx, game in enumerate(data):
            game_id, cubes = game.split(": ")
            game_id = parse("Game {}", game_id)[0]
            cubes = cubes.split("; ")
            for iteration in cubes:
                match_green, match_red, match_blue = pattern_matching(
                    iteration
                )
                if (
                    (match_blue and int(match_blue.group(1)) > bag["blue"])
                    or (match_red and int(match_red.group(1)) > bag["red"])
                    or (
                        match_green
                        and int(match_green.group(1)) > bag["green"]
                    )
                ):
                    break

            else:
                if game_id != None:
                    sum_of_ids += int(game_id)
        return sum_of_ids

    if part == "part_2":
        sum_of_powers = 0
        for game in data:
            game_id, cubes = game.split(": ")
            cubes = cubes.split("; ")

            red, green, blue = 0, 0, 0

            for iteration in cubes:
                match_green, match_red, match_blue = pattern_matching(
                    iteration
                )

                if match_blue and int(match_blue.group(1)) > blue:
                    blue = int(match_blue.group(1))
                if match_green and int(match_green.group(1)) > green:
                    green = int(match_green.group(1))
                if match_red and int(match_red.group(1)) > red:
                    red = int(match_red.group(1))

            powers = red * blue * green
            sum_of_powers += powers

        return sum_of_powers


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]
        print(day_two(data, "part_1"))
        print(day_two(data, "part_2"))
