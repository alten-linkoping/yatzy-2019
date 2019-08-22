from dataclasses import dataclass, field, fields
from typing import Optional, Callable, List, Iterator, Tuple, Dict
from abc import ABC, abstractmethod # Python built-in abstract class package

@dataclass(init=False, repr=False)
class ScoreSectionBase(ABC):
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
                yield field.name.strip("_"), getattr(score_section, field.name)
        return iterator_fkn(self)

    def total_score(self) -> int:
        """
            Calculate total score.
        """
        _total_score = 0
        for _, score in self:
            if score is not None:
                _total_score += score
        return _total_score

    def to_dict(self) -> Dict[str, int]:
        dict_repr = {name:score for name, score in self}
        dict_repr["total_score"] = self.total_score()
        return dict_repr

    @property
    def unused_fields(self):
        return [name for name, score in self if score is None]

    @property
    def field_names(self):
        return [name for name, _ in self]

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

@dataclass(init=False, repr=False)
class UpperSectionScore(ScoreSectionBase):
    once    :Optional[int] = field(default=None) 
    twos    :Optional[int] = field(default=None)
    threes  :Optional[int] = field(default=None)
    fours   :Optional[int] = field(default=None)
    fives   :Optional[int] = field(default=None)
    sixes   :Optional[int] = field(default=None)
    _bonus  :Optional[int] = field(default=None)

    def __init__(self, bonus_rule: Callable[[int], Optional[int]]):
        self.bonus_rule = bonus_rule

    def __setattr__(self, name, value):
        self.__dict__[name] = value
        # If it is a defined fields (values we care about) check for bonus points
        if name in [field.name for field in fields(self)]:
            bonus_score = self.bonus_rule(self.total_score())
            if bonus_score is not None:
                # Set score for bonus, without calling this method again
                self.__dict__["_bonus"] = bonus_score