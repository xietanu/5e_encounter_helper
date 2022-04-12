"""Classes for describing monster sizes"""
from dataclasses import dataclass
from enum import Enum

from dnd import dice


@dataclass
class SizeData:
    """Contains data needed to handle monster sizes"""

    label: str
    die: dice.Die
    damage_dice: int
    token_size: int


class Sizes(SizeData, Enum):
    """Possible Monster sizes"""

    TINY = "Tiny", dice.Die(4), 1, 1
    SMALL = "Small", dice.Die(6), 1, 1
    MEDIUM = "Medium", dice.Die(8), 1, 1
    LARGE = "Large", dice.Die(10), 2, 2
    HUGE = "Huge", dice.Die(12), 3, 3
