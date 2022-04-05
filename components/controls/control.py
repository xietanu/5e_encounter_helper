"""Filter class for users to specify the data they want to see"""
from dataclasses import dataclass
from typing import Optional

from dash import html


@dataclass
class Control:
    """
    A Control is used by the dashboard to get information from users
    to specify what data to display.

    This is a generic parent class for types of controls to be built off of.
    """

    identifier: str
    label: str
    default_value: str

    def _create_interactice_element_html(self, selected_value: str):
        raise NotImplementedError()

    def to_html(self, selected_value: Optional[str] = None) -> html.Div:
        """
        Creates a HTML representation of the filter.

        Dummy function to be built on top of for child classes.

        Args:
            selected_value (str, optional): Currently selected value. Defaults to None.

        Returns:
            html.Div: The HTML element representing the filter.
        """
        if selected_value is None:
            selected_value = str(self.default_value)

        return html.Div(
            [
                html.Label(
                    self.label + ":",
                    htmlFor=self.identifier,
                    className="card-element-label",
                ),
                self._create_interactice_element_html(selected_value),
                html.Div(
                    id=f"{self.identifier}-message", className="card-element-message"
                ),
            ],
            className="card-element",
        )
