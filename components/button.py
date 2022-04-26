from typing import Optional
from dash import html


def button(
    label: str,
    component_id: str,
    width: Optional[str] = None,
):
    """
    Button component with label

    Args:
        label (str): The text label for the button
        component_id (str): The id of the component

    Returns:
        html.Button: The button HTML element.
    """
    return html.Button(
        children=label,
        id=component_id,
        n_clicks=0,
        className="button-dnd",
        style={"width": width} if width else None,
    )
