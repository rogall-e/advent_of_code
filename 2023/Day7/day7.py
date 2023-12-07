from collections import  Counter
from functools import reduce

def day_seven(data, part):
    if part == "part_1":
        card_ranks = {
            "A": 0,
            "K": 1,
            "Q": 2,
            "J": 3,
            "T": 4,
            "9": 5,
            "8": 6,
            "7": 7,
            "6": 8,
            "5": 9,
            "4": 10,
            "3": 11,
            "2": 12,
        }


        hands = [[card_ranks[x] for x in _.split(" ")[0]] for _ in data]
        hand_ranks = [get_hand_ranks(hand) for hand in hands]  
    
    if part == "part_2":
        card_ranks = {
            "A": 0,
            "K": 1,
            "Q": 2,
            "J": 12,
            "T": 3,
            "9": 4,
            "8": 5,
            "7": 6,
            "6": 7,
            "5": 8,
            "4": 9,
            "3": 10,
            "2": 11,
        }

        hands = [[card_ranks[x] for x in _.split(" ")[0]] for _ in data]
        hand_ranks = [get_hand_ranks(hand) for hand in hands]
        for idx,hand in enumerate(hands):
            for card_value in card_ranks.values():
                hand_ranks[idx] = min(hand_ranks[idx], get_hand_ranks(
                    reduce(lambda a,b: a + [card_value] if b == 12 else a + [b], hand, [])
                    ))
            
    


    bids = [int(_.split(" ")[1]) for _ in data]
    solution = [(a,b,c) for a,b,c in zip(hand_ranks, hands, bids)]

    solution.sort(reverse=True)
    
    return sum((idx + 1) * x[-1] for idx, x in enumerate(solution))

def get_hand_ranks(hand):
    match [b for _, b in Counter(hand).most_common()]:
        case 5, *_:
            return 1
        case 4, *_:
            return 2
        case 3, 2, *_:
            return 3
        case 3, *_:
            return 4
        case 2,2, *_:
            return 5
        case 2, *_:
            return 6
        case _:
            return 7
        

if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]
        print(day_seven(data, "part_1"))
        print(day_seven(data, "part_2"))
