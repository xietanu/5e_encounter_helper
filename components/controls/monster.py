"""Monster enum"""
from enum import Enum
from components.controls import number, dropdown
import dnd


class Monster(Enum):
    """List of monster related controls"""

    CR = number.Number(
        label="CR",
        identifier="challenge_rating",
        default_value="1",
    )

    FAMILY = dropdown.Dropdown(
        label = "Type",
        identifier = "family",
        options = [family.value.name for family in dnd.Family]
    )
