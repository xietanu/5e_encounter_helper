"""Card component for containing dashboard elements"""
from typing import Union

from dash import html


def card_row(cards: Union[html.Div, list[html.Div]]) -> html.Div:
    """
    Creates a horizontal row used to contain cards. The card and card_row work together to create a
    layout that stretches and shrinks when the user changes the size of the window, or accesses the
    dashboard from a mobile device.

    Args:
        cards (list[html.Div]): List of card <div> elements

    Returns:
        html.Div: The card row element
    """
    return html.Div(
        cards,
        className="card-row",
    )


def card(children: list, element_id: str = "") -> html.Div:
    """
    A rectangle with an off-white background.
    Used to wrap individual elements of a dashboard.

    Args:
        children (list): HTML elements making up the content of the card.
        element_id (str, optional): id to assign to card for targeting with react elements.
            Defaults to None.

    Returns:
        html.Div: The card HTML element
    """
    if element_id:
        return html.Div(children, className="card", id=element_id)
    return html.Div(children, className="card")


def card_section(children: list) -> html.Div:
    """
    Sub-section to divide up contents in a card

    Args:
        children (list): Contents of the section

    Returns:
        html.Div: Contains the section
    """
    return html.Div(children, className="card-section")


def card_element_row(children: list) -> html.Div:
    """
    Creates a wrappable row of card elements

    Args:
        children (list): _description_

    Returns:
        html.Div: _description_
    """
    return html.Div(children, className="card-element-row")


def card_element(label: str, value: str) -> html.Div:
    """
    Standard label and description for a stat-block.

    Args:
        label (str): The label for the element.
        value (str): The contents of the element.

    Returns:
        html.Div: Contains the stat block element.
    """
    return html.Div(
        [
            html.Div(label, className="card-element-label"),
            html.Div(value, className="card-element-value"),
        ],
        className="card-element",
    )
