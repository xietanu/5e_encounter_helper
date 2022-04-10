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


def subtitle(title: str) -> html.Div:
    return html.Div(title, className="dnd-hint")
