"""Number Control"""
from dataclasses import dataclass
from dash import dcc, Input, Output
from app import app
from components.controls import control


@dataclass(frozen=True)
class NumberControl(control.Control):
    """
    A control that allows the user to input an integer.
    """

    def _create_interactice_element_html(self, selected_value: str):
        return dcc.Input(
            id=self.identifier,
            value=str(selected_value),
            className="card-element-value",
            style={"width": f"{max(1.8,len(str(selected_value))*0.6)}em"},
        )

    def _init_callback(self):
        @app.callback(
            Output(
                component_id=f"{self.identifier}-message", component_property="children"
            ),
            Input(component_id=f"{self.identifier}", component_property="value"),
        )
        def update_message(value: str) -> str:
            if not value.isnumeric():
                return "Input should be number"
            return ""
