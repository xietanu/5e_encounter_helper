"""Component that allows the user to select options from a pre-determined list"""
from typing import Optional

import dash
from components.controls.control import Control


class Slider(Control):
    """
    A filter that allows the user to select options from a pre-determined list.
    """

    def __init__(
        self,
        label: str,
        identifier: str,
        min_max_range: tuple[int, int],
        default_value: int,
    ):
        """
        Args:
            title (str): Label to use for the filter
            filter_id (str): Variable name to be used for the filter.
            options (list): List of pre-determined options for the user to pick from.
            default_value (str, optional): Default option to be selected. Defaults to None.
        """
        super().__init__(label, identifier, default_value)
        self.min, self.max = min_max_range

    def to_html(self, selected_value: Optional[int] = None) -> dash.html.Div:
        """
        Returns a HTML dropdown representing the filter for the user to select an option from.

        Args:
            selected_value (str, optional): Currently selected option. Defaults to None.

        Returns:
            html.Div: The HTML element representing the filter
        """
        if selected_value is None:
            selected_value = int(self.default_value)

        return dash.html.Div(
            [
                dash.html.Label(
                    self.label,
                    htmlFor=self.identifier,
                ),
                dash.dcc.Slider(
                    id=self.identifier,
                    min=self.min,
                    max=self.max,
                    step=1,
                    value=selected_value,
                ),
            ],
        )
