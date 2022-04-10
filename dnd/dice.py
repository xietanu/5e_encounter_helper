from dataclasses import dataclass


@dataclass
class Die:
    sides: int

    def __init__(self, sides: int):
        self.sides = sides
        self.average_value = float(sides) / 2 + 0.5

    def __str__(self):
        return f"d{self.sides}"


@dataclass
class DiceFormula:
    dice_count: int
    die: Die
    modifier: int

    def __str__(self):
        if self.modifier == 0:
            return f"{self.dice_count}{str(self.die)}"
        return f"{self.dice_count}{str(self.die)} {'+' if self.modifier > 0 else '-'} {abs(self.modifier)}"

    @property
    def average_value(self) -> int:
        return round(self.dice_count * self.die.average_value) + self.modifier
