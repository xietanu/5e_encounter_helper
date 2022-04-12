"""Classes describing standard D&D dice"""
from dataclasses import dataclass


@dataclass
class Die:
    """Data describing a die with a given number of sides"""

    sides: int

    def __init__(self, sides: int):
        self.sides = sides
        self.average_value = float(sides) / 2 + 0.5

    def __str__(self):
        return f"d{self.sides}"


@dataclass
class DiceFormula:
    """Class describing a number of dice with a modifier,
    a common way of representing value in D&D"""

    dice_count: int
    die: Die
    modifier: int

    def __str__(self):
        if self.modifier == 0:
            return f"{self.dice_count}{str(self.die)}"
        return (
            f"{self.dice_count}{str(self.die)} "
            f"{'+' if self.modifier > 0 else '-'} "
            f"{abs(self.modifier)}"
        )

    @property
    def average_value(self) -> int:
        """
        Calculate the mean value expected if rolling this set of dice plus the modifier.

        Returns:
            int: _description_
        """
        return round(self.dice_count * self.die.average_value) + self.modifier
