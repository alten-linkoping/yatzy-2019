import random
from typing import Optional, List
from collections import Counter

"""
    Module implementing the different rules of Yatzy.
    Most of these depends on a set of dice values to determine the score.
    The rules are based on: https://en.wikipedia.org/wiki/Yatzy
"""

def lower_section(dice: List[int], number:int) -> Optional[int]:
    return dice.count(number)*number if dice.count(number)*number != 0 else None


def small_straight(dice: List[int]) -> Optional[int]:
    return 15 if sorted(dice) == [1, 2, 3, 4, 5] else None


def large_straight(dice: List[int]) -> Optional[int]:
    return 20 if sorted(dice) == [2, 3, 4, 5, 6] else None


def one_pair(dice: List[int]) -> Optional[int]:
    PairList = []
    for x in Counter(dice):
        if(Counter(dice)[x] >= 2):
            PairList.append(x)
    if(len(PairList) != 0):
        return max(PairList)*2 
    return None


def two_pairs(dice: List[int]) -> Optional[int]:
    PairList = []
    for x in Counter(dice):
        if(Counter(dice)[x] >= 2):
            PairList.append(x)
    if(len(PairList) == 2):
        return PairList[0]*2 + PairList[1]*2
    return None


def three_of_a_kind(dice: List[int]) -> Optional[int]:
    DiceNumber = list(set([x for x in dice if dice.count(x) > 2]))
    return DiceNumber[0]*3 if DiceNumber else None


def four_of_a_kind(dice: List[int]) -> Optional[int]:
    DiceNumber = list(set([x for x in dice if dice.count(x) > 3]))
    return DiceNumber[0]*4 if DiceNumber else None


def yatzy(dice: List[int]) -> Optional[int]:
    return 50 if list(set([x for x in dice if dice.count(x) > 4])) else None


def full_house(dice: List[int]) -> Optional[int]:
    numberOfOccurrences = Counter(dice)
    for x in numberOfOccurrences:
        if(numberOfOccurrences[x] > 2):
            for y in numberOfOccurrences:
                if numberOfOccurrences[y] > 1 and x != y:
                    return x*3 + y*2

    return None

def chance(dice: List[int]) -> int:
    return sum(dice)

def bonus(upper_section_score: int) -> Optional[int]:
    """
        This rule is special as it depends on the total score of the upper section
        rather than on any dice.
    """
    return 50 if upper_section_score >= 63 else None