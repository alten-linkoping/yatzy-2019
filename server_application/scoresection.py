from dataclasses import dataclass, field, fields
from typing import Optional, Callable, List, Iterator, Tuple, Dict
from abc import ABC, abstractmethod # Python built-in abstract class package
from functools import partial
import rules

# "type: ignore" added to hide mypy error: 'Only concrete class can be given where "Type[ScoreSectionBase]" is expected'
# It is a known issue with abstract dataclasses https://github.com/python/mypy/issues/5374
@dataclass(init=False, repr=False)
class ScoreSectionBase(ABC): # type:ignore
    """
        The score base class. 
        IMPORTANT: When inheriting from this class the subclass needs to be
        decorated with the @dataclass decorator, as the methods depends on
        dataclass functionality.
    """
    def __repr__(self):
        lines:List[str] = []
        for field, score in self:
            lines.append(f'{field}: {score}')
        return "\n".join(lines)

    def __iter__(self) -> Iterator[Tuple[str, int]]:
        def iterator_fkn(score_section: ScoreSectionBase):
            for field in fields(score_section):
                yield field.name, getattr(score_section, field.name)
        return iterator_fkn(self)

    def total_score(self) -> int:
        """
            Calculate total score.
        """
        _total_score = 0
        for _, score in self.__iter__():
            if score is not None:
                _total_score += score
        return _total_score

    def to_dict(self) -> Dict[str, int]:
        dict_repr = {name:score for name, score in self}
        dict_repr["total_score"] = self.total_score()
        return dict_repr

    @property
    def unused_fields(self) -> List[str]:
        return [name for name, score in self if score is None and name[0] != "_"]

    @property
    def field_names(self) -> List[str]:
        return [name for name, _ in self]

    @abstractmethod
    def possible_actions(self, dice: List[int]) -> Dict[str, int]:
        raise NotImplementedError

@dataclass(init=False, repr=False)
class LowerSectionScore(ScoreSectionBase):
    one_pair        :Optional[int] = field(default=None)
    two_pairs       :Optional[int] = field(default=None)
    three_of_a_kind :Optional[int] = field(default=None)
    four_of_a_kind  :Optional[int] = field(default=None)
    small_straight  :Optional[int] = field(default=None)
    large_straight  :Optional[int] = field(default=None)
    full_house      :Optional[int] = field(default=None)
    chance          :Optional[int] = field(default=None)
    yatzy           :Optional[int] = field(default=None)

    def __init__(self):
        self._STANDARD_RULES_MAPPING: Dict["str", Callable[[List[int]], Optional[int]]] = dict(
            one_pair=rules.one_pair,
            two_pairs=rules.two_pairs,
            three_of_a_kind=rules.three_of_a_kind,
            four_of_a_kind=rules.four_of_a_kind,
            small_straight=rules.small_straight,
            large_straight=rules.large_straight,
            full_house=rules.full_house,
            chance=rules.chance,
            yatzy=rules.yatzy,
        )

    def possible_actions(self, dice: List[int]) -> Dict[str, int]:
        actions_scores: Dict[str, int] = dict()
        for field_name in self.unused_fields:
            rule_fkn = self._STANDARD_RULES_MAPPING[field_name]
            score = rule_fkn(dice)
            actions_scores[field_name] = score if score is not None else 0
        return actions_scores


@dataclass(init=False, repr=False)
class UpperSectionScore(ScoreSectionBase):
    once    :Optional[int] = field(default=None) 
    twos    :Optional[int] = field(default=None)
    threes  :Optional[int] = field(default=None)
    fours   :Optional[int] = field(default=None)
    fives   :Optional[int] = field(default=None)
    sixes   :Optional[int] = field(default=None)
    _bonus  :Optional[int] = field(default=None)

    def __init__(self):
        self._STANDARD_RULES_MAPPING: Dict["str", Callable[[List[int]], Optional[int]]] = dict(
            once=partial(rules.lower_section, number=1),
            twos=partial(rules.lower_section, number=2),
            threes=partial(rules.lower_section, number=3),
            fours=partial(rules.lower_section, number=4),
            fives=partial(rules.lower_section, number=5),
            sixes=partial(rules.lower_section, number=6),
        )
        self._BONUS_RULE: Callable[[int], Optional[int]] = rules.bonus

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        # If it is a defined fields (values we care about) check for bonus points
        if name in [field.name for field in fields(self)]:
            bonus_score = self._BONUS_RULE(self.total_score())
            if bonus_score is not None:
                # Set score for bonus, without calling this method again
                self.__dict__["_bonus"] = bonus_score

    
    def possible_actions(self, dice: List[int]) -> Dict[str, int]:
        actions_scores: Dict[str, int] = dict()
        for field_name in self.unused_fields:
            if field_name[0] == "_":
                # if it is a private field do nothing
                continue
            rule_fkn = self._STANDARD_RULES_MAPPING[field_name]
            score = rule_fkn(dice)
            actions_scores[field_name] = score if score is not None else 0
        return actions_scores
