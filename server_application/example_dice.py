import rules
import json
def points():
    dice = rules.roll_dice()
    return json.dumps({
        "dice": sorted(dice),
        "upper": {
            "SmallStraight": rules.SmallStraight(dice),
            "BigStraight": rules.BigStraight(dice),
            "One pair": rules.OnePair(dice),
            "Two pairs": rules.TwoPairs(dice),
            "three of": rules.ThreeOf(dice),
            "four of": rules.FourOf(dice),
            "yatzy!": rules.yatzy(dice),
            "full house!": rules.FullHouse(dice),
            "chance": rules.chance(dice)
        },
        "lower": {
            "ones": rules.LowerSection(dice, 1),
            "twos": rules.LowerSection(dice, 2),
            "threes": rules.LowerSection(dice, 3),
            "fours": rules.LowerSection(dice, 4),
            "fives": rules.LowerSection(dice, 5),
            "sixes": rules.LowerSection(dice, 6)

        }
    }
    )