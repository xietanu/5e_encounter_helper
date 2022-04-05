"""Filter class for users to specify the data they want to see"""
from typing import Optional, Union

from dash import html


class Control:
    """
    A Filter is used by the dashboard to get information from users
    to specify what data to display.

    This is a generic parent class for types of controls to be built off of.
    """

    def __init__(
        self, label: str, identifier: str, default_value: Union[str, int] = ""
    ) -> None:
        """
        Args:
            title (str): Label for the filter to display to the user
            filter_id (str): Internal variable used to identify the filter
            default_value (str): Any default value to use before the user has made a selection.
                Defaults to None.
        """
        self.label = label
        self.identifier = identifier
        self.default_value = default_value
        
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
                    self.label+':', htmlFor=self.identifier, className="card-element-label"
                ),
                self._create_interactice_element_html(selected_value),
                html.Div(
                    id = f"{self.identifier}-message",
                    className='card-element-message'
                )
            ],
            className="card-element",
        )
