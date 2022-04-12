"""Text area input"""
from dataclasses import dataclass
from enum import Enum

from dash import dcc

from components.controls.control import Control


@dataclass(frozen=True)
class TextAreaControl(Control):
    """
    A control that allows the user to input a short piece of text.
    """

    cols: int = 30
    rows: int = 1

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Textarea(
            id=self.identifier,
            value=selected_value,
            cols=self.cols,
            rows=self.rows,
        )


class TextArea(TextAreaControl, Enum):
    """Text area inputs"""

    TRAITS = "traits", "", "Example. An example trait.", 50, 6
