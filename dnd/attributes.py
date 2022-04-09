"""Attribute classes"""
from dataclasses import dataclass

from dash import html

from dnd import armours


@dataclass
class AttributeData:
    """Class for data associated with an individual attribute"""

    name: str
    modifier: int = 0

    @property
    def value(self) -> int:
        """
        Calculates the overall value associated with the modifier

        Returns:
            int: Attribute's value
        """
        return 10 + (self.modifier * 2)

    @property
    def short_name(self) -> str:
        """
        Returns:
            str: 3 letter name of the attribute
        """
        return self.name[:3]

    def to_html(self) -> html.Div:
        """
        Creates an HTML representation of the attribute

        Returns:
            html.Div: The attribute with title, value and modifier.
        """
        return html.Div(
            [
                html.Div(self.short_name.upper(), className="attribute-title"),
                html.Div(
                    f'{self.value} ({"+" if self.modifier >= 0 else ""}{self.modifier})',
                    className="attribute-value",
                ),
            ],
            className="attribute-block",
        )


class Attributes:
    """Class for a monster's attributes"""

    def __init__(self):
        self.str = AttributeData("Strength")
        self.dex = AttributeData("Dexterity")
        self.con = AttributeData("Constitution")
        self.int = AttributeData("Intelligence")
        self.wis = AttributeData("Wisdom")
        self.cha = AttributeData("Charisma")

    def __iter__(self):
        return iter([self.str, self.dex, self.con, self.int, self.wis, self.cha])

    def update_dex(
        self, expected_ac: int, armour_class_bonus: int, armour: armours.ArmourData
    ) -> None:
        """
        Update the dexterity based on aspects of the monster.

        Args:
            expected_ac (int): Expected armour class given CR
            armour_class_bonus (int): Any armour class bonus (e.g. from shields)
            armour (armours.ArmourData): Current armour used by the monster
        """
        self.dex.modifier = min(
            expected_ac - armour_class_bonus - armour.base_ac, armour.max_dex_mod
        )
