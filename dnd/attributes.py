"""Attribute classes"""
from dataclasses import dataclass

from dash import html

from dnd import armours


@dataclass
class AttributeData:
    """Class for data associated with an individual attribute"""

    name: str
    base_modifier: int = 0
    calc_modifier: int = 0
    
    @property
    def modifier(self) -> int:
        return self.base_modifier + self.calc_modifier

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

    def __init__(
        self,
        strength: int = 0,
        dex: int = 0,
        con: int = 0,
        intelligence: int = 0,
        wis: int = 0,
        cha: int = 0,
    ) -> None:
        self.str = AttributeData("Strength", strength)
        self.dex = AttributeData("Dexterity", dex)
        self.con = AttributeData("Constitution", con)
        self.int = AttributeData("Intelligence", intelligence)
        self.wis = AttributeData("Wisdom", wis)
        self.cha = AttributeData("Charisma", cha)

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
        self.dex.calc_modifier = (
            min(expected_ac - armour_class_bonus - armour.base_ac, armour.max_dex_mod)
        )
