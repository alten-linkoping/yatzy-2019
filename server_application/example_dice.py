import rules
import json

def roll_dice():
    dice = []
    for x in range(0, 5):
        dice.append(random.randint(1, 6))
    return dice


def points():
    dice = roll_dice()
    return json.dumps({
        "dice": sorted(dice),
        "upper": {
            "small_straight": rules.small_straight(dice),
            "large_straight": rules.large_straight(dice),
            "one_pair": rules.one_pair(dice),
            "two_pairs": rules.two_pairs(dice),
            "three_of_a_kind": rules.three_of_a_kind(dice),
            "four_of_a_kind": rules.four_of_a_kind(dice),
            "yatzy": rules.yatzy(dice),
            "full_house": rules.full_house(dice),
            "chance": rules.chance(dice)
        },
        "lower": {
            "ones": rules.lower_section(dice, 1),
            "twos": rules.lower_section(dice, 2),
            "threes": rules.lower_section(dice, 3),
            "fours": rules.lower_section(dice, 4),
            "fives": rules.lower_section(dice, 5),
            "sixes": rules.lower_section(dice, 6)

        }
    }
    )