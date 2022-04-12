"""Component that allows the user to select options from a pre-determined list"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from dash import html, dcc
from components.controls import control
import formatting


@dataclass(frozen=True)
class SliderControl(control.Control):
    """
    A filter that allows the user to select options from a pre-determined list.
    """

    min_max_range: tuple[int, int]
    mark_values: Optional[tuple[str]] = None
    mark_labels: Optional[tuple[str]] = None
    mark_freq: int = 1

    def _create_interactice_element_html(self, selected_value: str):
        if self.mark_values and self.mark_labels:
            marks = {
                value: label for label, value in zip(self.mark_labels, self.mark_values)
            }

        else:
            marks = {
                str(value): str(value)
                for value in range(self.min_max_range[0], self.min_max_range[1] + 1)
            }

        displayed_marks = {
            str(key_value[0]): str(key_value[1])
            for index, key_value in enumerate(marks.items())
            if index % self.mark_freq == 0 or index == len(marks) - 1
        }

        pixel_width = (
            30 * (self.min_max_range[1] - self.min_max_range[0] + 1)
        ) // self.mark_freq

        return html.Div(
            dcc.Slider(
                id=self.identifier,
                min=self.min_max_range[0],
                max=self.min_max_range[1],
                marks=displayed_marks,
                step=1,
                value=int(selected_value),
            ),
            style={
                "width": f"{pixel_width}px",
            },
        )


class Sliders(SliderControl, Enum):
    """Slider controls used in the dashboard"""

    CR = (
        "challenge_rating",
        "CR",
        "1",
        (-3, 30),
        tuple(str(value) for value in range(-3, 31)),
        tuple(formatting.format_challenge_rating(value) for value in range(-3, 31)),
        1,
    )
