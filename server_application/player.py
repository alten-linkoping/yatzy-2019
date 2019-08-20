from typing import List, Dict, Any
from scoresection import UpperSectionScore, LowerSectionScore

class Player:
    def __init__(self, name:str, upper_section: UpperSectionScore, lower_section:LowerSectionScore):
        self.name = name
        self.upper_section = upper_section
        self.lower_section = lower_section

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

    @property
    def unused_fields(self) -> List[str]:
        return self.upper_section.unused_fields + self.lower_section.unused_fields

    def is_finished(self):
        return not self.unused_fields

    def set_field(self, field_name: str, score:int):
        if field_name in self.upper_section.field_names:
            setattr(self.upper_section, field_name, score)
        elif field_name in self.lower_section.field_names:
            setattr(self.lower_section, field_name, score)
        else:
            raise AttributeError(f'No field, {field_name} available in any section')