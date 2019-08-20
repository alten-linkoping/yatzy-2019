import random
from collections import Counter


def roll_dice():
    dice = []
    for x in range(0, 5):
        dice.append(random.randint(1, 6))
    return dice


def LowerSection(dice, number):
    return dice.count(number)*number if dice.count(number)*number != 0 else None


def SmallStraight(dice):
    return 15 if sorted(dice) == [1, 2, 3, 4, 5] else None


def BigStraight(dice):
    return 20 if sorted(dice) == [2, 3, 4, 5, 6] else None


def OnePair(dice):
    PairList = []
    for x in Counter(dice):
        if(Counter(dice)[x] >= 2):
            PairList.append(x)
    if(len(PairList) != 0):
        return max(PairList)*2 
    return None


def TwoPairs(dice):
    PairList = []
    for x in Counter(dice):
        if(Counter(dice)[x] >= 2):
            PairList.append(x)
    if(len(PairList) == 2):
        return PairList[0]*2 + PairList[1]*2
    return None


def ThreeOf(dice):
    DiceNumber = list(set([x for x in dice if dice.count(x) > 2]))
    return DiceNumber[0]*3 if DiceNumber else None


def FourOf(dice):
    DiceNumber = list(set([x for x in dice if dice.count(x) > 3]))
    return DiceNumber[0]*4 if DiceNumber else None


def yatzy(dice):
    return 50 if list(set([x for x in dice if dice.count(x) > 4])) else None


def FullHouse(dice):
    numberOfOccurrences = Counter(dice)
    for x in numberOfOccurrences:
        if(numberOfOccurrences[x] > 2):
            for y in numberOfOccurrences:
                if numberOfOccurrences[y] > 1 and x != y:
                    return x*3 + y*2

    return None


def chance(dice):
    return sum(dice)