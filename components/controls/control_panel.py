"""Functions to create a control page for a dashboard page"""
from typing import Union
from components.controls import control
from components import cards, sections

GroupedControlList = dict[str, list[Union[control.Control, list[control.Control]]]]


def create_control_panel(control_groups: GroupedControlList, **control_kwargs):
    """
    Create a control panel for a page on the dashboard

    Args:
        controls (list[control.Control]): list of controls

    Returns:
        _type_: _description_
    """

    controls_html = []
    for title, control_group in control_groups.items():
        controls_lines = []
        for control_line in control_group:
            if isinstance(control_line, control.Control):
                controls_lines.append(
                    control_line.to_html(control_kwargs[control_line.identifier][0])
                )
            else:
                controls_lines.append(
                    cards.card_element_row(
                        [
                            user_control.to_html(
                                control_kwargs[user_control.identifier][0]
                            )
                            for user_control in control_line
                        ]
                    )
                )
        controls_html.append(
            cards.card([sections.collapsible_section(title, controls_lines)])
        )

    return cards.card_row(controls_html, style={"width": "100%"})
