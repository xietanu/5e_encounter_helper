"""Monster speed class"""
from dataclasses import dataclass
from enum import Enum

import formatting


class SpeedNames(Enum):
    """List of the speeds that monsters can have"""

    BASIC = "basic_speed"
    FLY = "fly"
    HOVER = "hover"
    BURROW = "burrow"
    CLIMB = "climb"
    SWIM = "swim"


@dataclass
class SpeedData:
    """Class for representing an individual speed"""

    name: str
    distance: int

    def __str__(self):
        return f"{self.name} {self.distance}ft."


class Speeds:
    """Class for representing monster speeds."""

    def __init__(self, **speed_values):
        self._speeds = {}
        for speed_name in SpeedNames:
            printed_speed_name = speed_name.value
            if printed_speed_name == "basic_speed":
                printed_speed_name = ""
            if speed_name.value in speed_values:
                self._speeds[speed_name.value] = SpeedData(
                    printed_speed_name,
                    formatting.defaulted_int(speed_values[speed_name.value], 0),
                )
            else:
                self._speeds[speed_name.value] = SpeedData(
                    printed_speed_name,
                    0,
                )

    def __getattr__(self, attribute_name: str) -> SpeedData:
        return self._speeds[attribute_name]

    def __iter__(self):
        return iter(
            speed_type
            for speed_type in [
                self.basic_speed,
                self.fly,
                self.hover,
                self.burrow,
                self.climb,
                self.swim,
            ]
            if speed_type.distance > 0
        )
