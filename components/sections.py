"""Components for sections in the page"""
from dash import html


def card_section(children: list) -> html.Div:
    """
    Sub-section to divide up contents in a card

    Args:
        children (list): Contents of the section

    Returns:
        html.Div: Contains the section
    """
    return html.Div(children, className="card-section")


def collapsible_section(title: str, children: list) -> html.Details:
    """
    Collapsible section, with given title.

    Args:
        title (str): Summary of the section
        children (list): Contents of the collapsible section

    Returns:
        html.Details: Collapsible section html.
    """
    return html.Details(
        children=[html.Summary(title)] + children,
        className="card-section",
        open=True,
    )
