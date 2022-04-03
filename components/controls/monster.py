"""Monster enum"""
from enum import Enum
from components.controls import slider


class Monster(Enum):
    """List of monster related controls"""

    CR = slider.Slider(
        label="CR",
        identifier="challenge_rating",
        min_max_range=(0, 20),
        default_value=1,
    )
