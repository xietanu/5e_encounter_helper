"""Component that allows the user to select options from a pre-determined list"""
from dataclasses import dataclass
from dash import dcc

from components.controls.control import Control


@dataclass
class Dropdown(Control):
    """
    A control that allows the user to select options from a pre-determined list.
    """

    options: list

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Dropdown(
            id=self.identifier,
            options=self.options,
            value=selected_value,
            clearable=False,
            className="card-element-value",
            style={"width": f"{max(len(option) for option in self.options)*0.8}em"},
        )
