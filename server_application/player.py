from typing import List, Dict, Any, Optional, Union
from scoresection import UpperSectionScore, LowerSectionScore

class Player:
    def __init__(self, name:str, upper_section: Optional[UpperSectionScore] = None, lower_section:Optional[LowerSectionScore] = None):
        self.name = name
        self.upper_section = upper_section if upper_section is not None else UpperSectionScore()
        self.lower_section = lower_section if lower_section is not None else LowerSectionScore()

    def total_score(self):
        return self.upper_section.total_score() + self.lower_section.total_score()

    def __repr__(self):
        out:List[str] = []
        out.append(self.upper_section.__repr__())
        out.append("------------------------------")
        out.append(self.lower_section.__repr__())
        out.append("==============================")
        out.append(f'total score: {self.total_score()}')
        return "\n".join(out)

    def to_dict(self) -> Dict[str, Any]:
        return dict(
            name = self.name,
            total_score = self.total_score(),
            upper_section = self.upper_section.to_dict(),
            lower_section = self.lower_section.to_dict(),
        )

    def possible_actions(self, dice: List[int]) -> Dict [str, int]:
        return dict(
                **self.lower_section.possible_actions(dice),
                **self.upper_section.possible_actions(dice),
            )


    @property
    def unused_fields(self) -> List[str]:
        return self.upper_section.unused_fields + self.lower_section.unused_fields

    def is_finished(self):
        return not self.unused_fields

    def set_field(self, field_name: str, score:Union[int, str]):
        if field_name in self.upper_section.field_names:
            setattr(self.upper_section, field_name, score)
        elif field_name in self.lower_section.field_names:
            setattr(self.lower_section, field_name, score)
        else:
            raise AttributeError(f'No field, {field_name} available in any section')