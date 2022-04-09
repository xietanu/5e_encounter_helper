"""Armour classes"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class ArmourData:
    """Data to represent armour"""
    label: str
    base_ac: int
    max_dex_mod: Optional[int] = None


class Armours(ArmourData, Enum):
    """List of armour types"""
    NATURAL = "Natural", 10
    LIGHT = "Light", 11
    MEDIUM = "Medium", 14, 2
    HEAVY = "Heavy", 17, 0
