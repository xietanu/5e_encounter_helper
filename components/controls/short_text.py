"""Short text control"""
from dataclasses import dataclass
from enum import Enum
from dash import html
from components.controls import control

@dataclass(frozen=True)
class ShortTextControl(control.Control):
    """
    A control that allows the user to input a short piece of text.
    """
    expected_length:int = 10
    
    def _create_interactice_element_html(self, selected_value: str):
        return html.Span(
            id=self.identifier,
            children=str(selected_value),
            className="card-element-value control-short-text",
            contentEditable="true",
        )
        
    @property
    def component_property(self):
        return "children"


class ShortTexts(ShortTextControl, Enum):
    NAME = "name", "Name", "", 20