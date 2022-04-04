"""Component that allows the user to select options from a pre-determined list"""
from typing import Optional

import dash
from app import app
from components.controls import control


class Number(control.Control):
    """
    A filter that allows the user to select options from a pre-determined list.
    """

    def __init__(
        self,
        label: str,
        identifier: str,
        default_value: str = "0",
    ):
        """
        Args:
            title (str): Label to use for the filter
            filter_id (str): Variable name to be used for the filter.
            options (list): List of pre-determined options for the user to pick from.
            default_value (str, optional): Default option to be selected. Defaults to None.
        """
        super().__init__(label, identifier, default_value)
        
        @app.callback(
            dash.Output(component_id=f"{self.identifier}-type-message", component_property="children"),
            dash.Input(component_id=f"{self.identifier}", component_property="value")
        )
        def update_message(value:str) -> str:
            if not value.isnumeric():
                return "Input should be number"
            return ""

    def to_html(self, selected_value: Optional[str] = None) -> dash.html.Div:
        """
        Returns a HTML dropdown representing the filter for the user to select an option from.

        Args:
            selected_value (str, optional): Currently selected option. Defaults to None.

        Returns:
            html.Div: The HTML element representing the filter
        """
        if selected_value is None:
            selected_value = str(self.default_value)

        return dash.html.Div(
            [
                dash.html.Label(
                    self.label,
                    htmlFor=self.identifier,
                ),
                dash.dcc.Input(
                    id=self.identifier,
                    value=str(selected_value),
                ),
                dash.html.Div(
                    id = f"{self.identifier}-type-message"
                )
            ],
        )
