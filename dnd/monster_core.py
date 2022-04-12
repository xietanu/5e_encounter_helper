"""Class to hold core data about monsters"""
from dataclasses import dataclass
from typing import Union

from dnd import families, sizes
import formatting


@dataclass
class MonsterCoreData:
    """Holds core information about the type of the monster"""

    name: str = "Unnamed monster"
    challenge_rating: int = 1
    size: sizes.Sizes = sizes.Sizes.MEDIUM
    family: families.Families = families.Families.HUMANOID

    def __init__(
        self,
        name: str = "Unnamed monster",
        challenge_rating: Union[str, int] = 1,
        size: str = "MEDIUM",
        family: str = "HUMANOID",
    ):
        self.name = name
        self.challenge_rating = (
            int(challenge_rating) if formatting.is_intlike(challenge_rating) else 1
        )
        self.size = sizes.Sizes[size]
        self.family = families.Families[family]
