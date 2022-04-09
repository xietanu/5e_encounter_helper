"""Classes for describing monster sizes"""
from dataclasses import dataclass
from enum import Enum


@dataclass
class SizeData:
    """Contains data needed to handle monster sizes"""

    label: str
    die_name: str
    avg_die_value: float
    damage_dice: int
    token_size: int


class Sizes(SizeData, Enum):
    """Possible Monster sizes"""

    TINY = "Tiny", "d4", 2.5, 1, 1
    SMALL = "Small", "d6", 3.5, 1, 1
    MEDIUM = "Medium", "d8", 4.5, 1, 1
    LARGE = "Large", "d10", 5.5, 2, 2
    HUGE = "Huge", "d12", 6.5, 3, 3
