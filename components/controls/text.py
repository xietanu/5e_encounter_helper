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

    NAME = "monster_name", "Name", "", 20


@dataclass(frozen=True)
class NumberControl(control.Control):
    """
    A control that allows the user to input an integer.
    """

    min_value: int = 100
    max_value: int = -100

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Input(
            id=self.identifier,
            type="number",
            value=str(selected_value),
            className="card-element-value",
            style={"width": f"{max(2.5,len(str(selected_value))*0.6)}em"},
            min=self.min_value,
            max=self.max_value,
        )


class Numbers(NumberControl, Enum):
    """Integer text inputs"""

    ARMOUR_BONUS = ("armour_class_bonus", "Armour class bonus", "0", 0, 10)
