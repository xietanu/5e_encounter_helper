"""page_title function"""
from dash import html


def page_title(title: str) -> html.H1:
    """
    Create HTML for standard styled page title

    Args:
        title (str): page title

    Returns:
        dash.html.H1: title HTML component
    """
    return html.H1(title)


def section_title(title: str) -> html.H2:
    """
    Create HTML for standard styled page title

    Args:
        title (str): section title

    Returns:
        dash.html.H2: title HTML component
    """
    return html.H2(title)


def subtitle(text: str) -> html.Div:
    """
    Text to display below a title for additional information

    Args:
        text (str): Text to display.

    Returns:
        html.Div: The formatted text.
    """
    return html.Div(text, className="dnd-hint")
