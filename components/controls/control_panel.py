"""Functions to create a control page for a dashboard page"""
from typing import Union
from components.controls import control
from components import cards

GroupedControlList = list[Union[control.Control, list[control.Control]]]


def create_control_panel(control_groups: GroupedControlList, **control_kwargs):
    """
    Create a control panel for a page on the dashboard

    Args:
        controls (list[control.Control]): list of controls

    Returns:
        _type_: _description_
    """

    controls_html = []
    for control_group in control_groups:
        if isinstance(control_group, control.Control):
            controls_html.append(
                control_group.to_html(control_kwargs[control_group.identifier])
            )
        else:
            controls_html.append(
                cards.card_element_row(
                    [
                        user_control.to_html(control_kwargs[user_control.identifier])
                        for user_control in control_group
                    ]
                )
            )

    return cards.card_row(cards.card([cards.card_section(controls_html)]))
