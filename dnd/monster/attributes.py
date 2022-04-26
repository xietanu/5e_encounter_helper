"""Attribute classes"""
from dataclasses import dataclass
from enum import Enum

from dash import html

from dnd.monster import armours
import formatting


class AttributeNames(Enum):
    """Names of the 6 attributes"""

    STR = "strength"
    DEX = "dexterity"
    CON = "constitution"
    INT = "intelligence"
    WIS = "wisdom"
    CHA = "charisma"


@dataclass
class AttributeData:
    """Class for data associated with an individual attribute"""

    name: str
    base_modifier: int = 0
    calc_modifier: int = 0

    @property
    def modifier(self) -> int:
        """
        Calculates the modifier for this attribute

        Returns:
            int: The modifier for this attribute
        """
        return self.base_modifier + self.calc_modifier

    @property
    def value(self) -> int:
        """
        Calculates the overall value associated with this attribute

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

    def __init__(self, **base_modifiers) -> None:
        self._attributes = {}
        for attribute_name in AttributeNames:
            if attribute_name.value in base_modifiers:
                self._attributes[attribute_name.value] = AttributeData(
                    attribute_name.value,
                    formatting.defaulted_int(base_modifiers[attribute_name.value], 0),
                )
            else:
                self._attributes[attribute_name.value] = AttributeData(
                    attribute_name.value, 0
                )

    def __getattr__(self, attribute_name: str) -> AttributeData:
        return self._attributes[attribute_name]

    def __iter__(self):
        return iter([attribute for _, attribute in self._attributes.items()])
    
    def to_dict(self) -> dict[str,str]:
        """
        Convert attributes to a dictionary for saving.

        Returns:
            dict[str,str]: Dictionary of attributes with base modifiers.
        """
        return {
            name: str(attribute.base_modifier) for name, attribute in self._attributes.items()
        }

    def update_dex(
        self,
        expected_ac: int,
        armour_type: armours.ArmourData,
        armour_class_bonus: int,
    ) -> None:
        """
        Update the dexterity based on aspects of the monster.

        Args:
            expected_ac (int): Expected armour class given CR
            armour_class_bonus (int): Any armour class bonus (e.g. from shields)
            armour (armours.ArmourData): Current armour used by the monster
        """
        self._attributes[AttributeNames.DEX.value].calc_modifier = min(
            expected_ac - armour_class_bonus - armour_type.base_ac,
            armour_type.max_dex_mod,
        )
