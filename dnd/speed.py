"""Monster speed class"""
from dataclasses import dataclass

import formatting

@dataclass
class Speed:
    """Class for representing an individual speed"""
    name: str
    distance: int

    def __str__(self):
        return f'{self.name} {self.distance}ft.'


class Speeds:
    """Class for representing monster speeds."""
    def __init__(self,
    basic_speed: int = 30,
    flying: int = 0,
    hovering: int = 0,
    burrowing: int = 0,
    climbing: int = 0,
    swimming: int = 0,):
        self.basic_speed = Speed('', int(basic_speed) if formatting.is_intlike(basic_speed) else 0)
        self.flying = Speed('fly', int(flying) if formatting.is_intlike(flying) else 0)
        self.hovering = Speed('hover', int(hovering) if formatting.is_intlike(hovering) else 0)
        self.burrowing = Speed('burrow', int(burrowing) if formatting.is_intlike(burrowing) else 0)
        self.climbing = Speed('climb', int(climbing) if formatting.is_intlike(climbing) else 0)
        self.swimming = Speed('swim', int(swimming) if formatting.is_intlike(swimming) else 0)

    def __iter__(self):
        return iter(
            speed_type
            for speed_type in [
                self.basic_speed,
                self.flying,
                self.hovering,
                self.burrowing,
                self.climbing,
                self.swimming,
            ]
            if speed_type.distance > 0
        )
