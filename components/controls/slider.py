"""Component that allows the user to select options from a pre-determined list"""
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

    def _create_interactice_element_html(self, selected_value: str):
        return dash.dcc.Slider(
            id=self.identifier,
            min=self.min,
            max=self.max,
            step=1,
            value=int(selected_value),
            className="card-element-value",
        )
