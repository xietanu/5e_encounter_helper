"""Component that allows the user to select options from a pre-determined list"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from dash import html, dcc, Input, Output
from components.controls import control
from app import app


@dataclass(frozen=True)
class SliderControl(control.Control):
    """
    A filter that allows the user to select options from a pre-determined list.
    """

    min_max_range: tuple[int, int]
    mark_values: Optional[tuple[str]] = None
    mark_labels: Optional[tuple[str]] = None
    mark_freq: int = 1

    def _create_interactice_element_html(self, selected_value: str, marks: dict):
        displayed_marks = {
            str(key_value[0]): str(key_value[1])
            for index, key_value in enumerate(marks.items())
            if index % self.mark_freq == 0 or index == len(marks) - 1
        }

        return dcc.Slider(
            id=self.identifier,
            min=self.min_max_range[0],
            max=self.min_max_range[1],
            marks=displayed_marks,
            step=1,
            value=int(selected_value),
        )

    def to_html(self, selected_value: Optional[str] = None) -> html.Div:
        """
        Creates a HTML representation of the control.

        Args:
            selected_value (str, optional): Currently selected value. Defaults to None.

        Returns:
            html.Div: The HTML element representing the filter.
        """
        if selected_value is None:
            selected_value = str(self.default_value)

        if self.mark_values and self.mark_labels:
            marks = {
                value: label for label, value in zip(self.mark_labels, self.mark_values)
            }

        else:
            marks = {
                str(value): str(value)
                for value in range(self.min_max_range[0], self.min_max_range[1] + 1)
            }

        return html.Div(
            [
                html.Label(
                    self.label + ":",
                    htmlFor=self.identifier,
                    className="card-element-label",
                ),
                html.Div(
                    marks[str(selected_value)],
                    id=f"{self.identifier}-value",
                    className="card-element-value",
                    style={
                        "width": f"{max(len(label) for label in self.mark_labels)*0.6 if self.mark_labels else 1.5}em"
                    },
                ),
                html.Div(
                    self._create_interactice_element_html(selected_value, marks),
                    style={
                        "width": f"{(30*(self.min_max_range[1]-self.min_max_range[0]+1))//self.mark_freq}px",
                    },
                ),
            ],
            className="card-element centre-aligned",
        )

    def _add_callback(self):
        @app.callback(
            Output(
                component_id=f"{self.identifier}-value", component_property="children"
            ),
            Input(component_id=f"{self.identifier}", component_property="value"),
        )
        def update_readout(value: str) -> str:
            return value


class Sliders(SliderControl, Enum):
    """Slider controls used in the dashboard"""
    CR = (
        "challenge_rating",
        "CR",
        "0",
        (-3, 30),
        tuple(str(value) for value in range(-3, 31)),
        tuple(
            str(value) if value >= 0 else f"1\u2044{2**-value}"
            for value in range(-3, 31)
        ),
        3
    )
