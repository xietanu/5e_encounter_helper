"""Armour classes"""
from dataclasses import dataclass
from enum import Enum
from typing import Union

import formatting


@dataclass
class ArmourData:
    """Data to represent armour"""

    label: str
    base_ac: int
    max_dex_mod: int = 99


class ArmourTypes(ArmourData, Enum):
    """List of armour types"""

    NATURAL = "Natural", 10
    LIGHT = "Light", 11
    MEDIUM = "Medium", 14, 2
    HEAVY = "Heavy", 17, 0


@dataclass
class Armour:
    """Data on a monster's specific armour"""

    armour_type: ArmourTypes = ArmourTypes.NATURAL
    bonus: int = 0

    def __init__(
        self, armour_type: str = ArmourTypes.NATURAL.name, bonus: Union[str, int] = 0
    ):
        self.armour_type = ArmourTypes[armour_type]
        self.bonus = formatting.defaulted_int(bonus, 0)

    def to_dict(self) -> dict[str, str]:
        """
        Convert values to dictionary for saving

        Returns:
            dict[str,str]: The dictionary containing the configuration.
        """
        return {
            "armour_type": self.armour_type.name,
            "bonus": str(self.bonus),
        }
