"""Component that allows the user to select options from a pre-determined list"""
from dataclasses import dataclass
import dash
from components.controls.control import Control


@dataclass
class Slider(Control):
    """
    A filter that allows the user to select options from a pre-determined list.
    """

    min_max_range: tuple[int, int]

    def _create_interactice_element_html(self, selected_value: str):
        return dash.dcc.Slider(
            id=self.identifier,
            min=self.min_max_range[0],
            max=self.min_max_range[1],
            step=1,
            value=int(selected_value),
            className="card-element-value",
        )
