"""Component that allows the user to select options from a pre-determined list"""
from dataclasses import dataclass
import dash
from app import app
from components.controls import control


@dataclass
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
            label (str): Label to use for the control
            identifier (str): Variable name to be used for the control.
            default_value (str, optional): Default option to be selected. Defaults to "0".
        """
        super().__init__(label, identifier, default_value)

        @app.callback(
            dash.Output(
                component_id=f"{self.identifier}-message", component_property="children"
            ),
            dash.Input(component_id=f"{self.identifier}", component_property="value"),
        )
        def update_message(value: str) -> str:
            if not value.isnumeric():
                return "Input should be number"
            return ""

    def _create_interactice_element_html(self, selected_value: str):
        return dash.dcc.Input(
            id=self.identifier,
            value=str(selected_value),
            className="card-element-value",
            style={"width": f"{max(1.8,len(str(selected_value))*0.8)}em"},
        )
