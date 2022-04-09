"""Component that allows the user to select options from a pre-determined list"""
from dataclasses import dataclass
from enum import Enum
from dash import dcc

from components.controls import control
import dnd


@dataclass(frozen=True)
class DropdownControl(control.Control):
    """
    A control that allows the user to select options from a pre-determined list.
    """

    options_labels: tuple
    options_values: tuple

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Dropdown(
            id=self.identifier,
            options=[
                {"label": label, "value": value}
                for label, value in zip(self.options_labels, self.options_values)
            ],
            value=selected_value,
            clearable=False,
            className="card-element-value",
            style={
                "width": f"{max(len(option) for option in self.options_labels)*0.4+4}em"
            },
        )


class Dropdowns(DropdownControl, Enum):
    """Dropdown controls"""

    FAMILY = (
        "family",
        "Type",
        dnd.Families.HUMANOID.name,
        tuple(family.label for family in dnd.Families),
        tuple(family.name for family in dnd.Families),
    )

    SIZE = (
        "size",
        "Size",
        dnd.Sizes.MEDIUM.name,
        tuple(size.label for size in dnd.Sizes),
        tuple(size.name for size in dnd.Sizes),
    )

    ARMOUR = (
        "armour",
        "Armour",
        dnd.Armours.NATURAL.name,
        tuple(armour.label for armour in dnd.Armours),
        tuple(armour.name for armour in dnd.Armours),
    )
