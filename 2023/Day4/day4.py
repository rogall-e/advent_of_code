from collections import defaultdict


def day_four(data, part):
    cards = [_.split(": ")[1] for _ in data]

    winning_cards = [_.split(" | ")[0].strip() for _ in cards]
    elves_cards = [_.split(" | ")[1].strip() for _ in cards]

    winning_cards = [
        list(map(int, _winning.split())) for _winning in winning_cards
    ]
    elves_cards = [list(map(int, _elves.split())) for _elves in elves_cards]

    if part == "part_1":
        compare_cards(elves=elves_cards, winning=winning_cards)
    if part == "part_2":
        amount_cards = defaultdict(int)
        for _ in range(len(winning_cards)):
            amount_cards[f"Card { _ + 1 }"] = 1
        counting_cards(
            elves=elves_cards, winning=winning_cards, amount_cards=amount_cards
        )


def compare_cards(elves, winning, points=0, idx=0):
    if idx < len(winning):
        elves_set = set(elves[idx])
        winning_set = set(winning[idx])

    if idx == len(winning):
        print(points)
        solution = points
        return solution

    if points == 0:
        hits = elves_set.intersection(winning_set)
        points = 2 ** (len(hits) - 1)
        idx += 1
        return compare_cards(elves, winning, points, idx)

    else:
        hits = elves_set.intersection(winning_set)
        if len(hits) == 0:
            points = points
        else:
            points += 2 ** (len(hits) - 1)
        idx += 1
        return compare_cards(elves, winning, points, idx)


def counting_cards(elves, winning, amount_cards, idx=0):
    if idx < len(elves):
        elves_set = set(elves[idx])
        winning_set = set(winning[idx])

        hits = elves_set.intersection(winning_set)
        idx += 1
        if len(hits) > 0:
            for _ in range(1, len(hits) + 1):
                amount_cards[f"Card {idx + _}"] += amount_cards[f"Card {idx}"]

        counting_cards(elves, winning, amount_cards, idx)
    else:
        print(sum(amount_cards.values()))
        solution = sum(amount_cards.values())
        return solution


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]
        day_four(data, "part_1")
        day_four(data, "part_2")
