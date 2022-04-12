"""Text input controls"""
from dataclasses import dataclass
from enum import Enum
from dash import dcc
from components.controls import control


@dataclass(frozen=True)
class ShortTextControl(control.Control):
    """
    A control that allows the user to input a short piece of text.
    """

    expected_length: int = 10

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Input(
            id=self.identifier,
            type="text",
            value=selected_value,
            className="card-element-value",
            minLength=self.expected_length,
        )


class ShortTexts(ShortTextControl, Enum):
    """Short text inputs"""

    NAME = "name", "Name", "Unnamed Monster", 20


@dataclass(frozen=True)
class NumberControl(control.Control):
    """
    A control that allows the user to input an integer.
    """

    min_value: int = 100
    max_value: int = -100
    step: int = 1

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Input(
            id=self.identifier,
            type="number",
            value=str(selected_value),
            className="card-element-value",
            style={"width": f"{max(2.5,len(str(selected_value))*0.6)}em"},
            min=self.min_value,
            max=self.max_value,
            step=self.step,
        )


class Numbers(NumberControl, Enum):
    """Integer text inputs"""

    ARMOUR_BONUS = ("bonus", "Armour class bonus", "0", 0, 10)
    BASIC_SPEED = ("basic_speed", "Speed", "30", 0, 150, 5)
    FLYING = ("fly", "Flying", "0", 0, 150, 5)
    HOVERING = ("hover", "Hovering", "0", 0, 150, 5)
    BURROWING = ("burrow", "Burrowing", "0", 0, 150, 5)
    CLIMBING = ("climb", "Climbing", "0", 0, 150, 5)
    SWIMMING = ("swim", "Swimming", "0", 0, 150, 5)
    STR = ("strength", "Str", "0", -5, 5)
    DEX = ("dexterity", "Dex", "0", -5, 5)
    CON = ("constitution", "Con", "0", -5, 5)
    INT = ("intelligence", "Int", "0", -5, 5)
    WIS = ("wisdom", "Wis", "0", -5, 5)
    CHA = ("charisma", "Cha", "0", -5, 5)
