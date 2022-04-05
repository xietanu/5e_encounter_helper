"""Component that allows the user to select options from a pre-determined list"""
from components.controls.control import Control
from dash import dcc


class Dropdown(Control):
    """
    A filter that allows the user to select options from a pre-determined list.
    """

    def __init__(
        self,
        label: str,
        identifier: str,
        options: list,
        default_value: str = "",
    ):
        """
        Args:
            title (str): Label to use for the filter
            filter_id (str): Variable name to be used for the filter.
            options (list): List of pre-determined options for the user to pick from.
            default_value (str, optional): Default option to be selected. Defaults to None.
        """
        super().__init__(label, identifier, default_value)
        self.options = options

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Dropdown(
            id=self.identifier,
            options=self.options,
            value=selected_value,
            clearable=False,
            className="card-element-value",
            style={"width": f"{max(len(option) for option in self.options)*0.8}em"},
        )
