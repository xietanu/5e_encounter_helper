"""Component for displaying a monster's traits."""
from dash import html


def trait(title: str, value: str) -> html.Div:
    """
    Component for displaying the title and contents of a monster's trait.

    Args:
        title (str): Trait's title
        value (str): Trait's contents.

    Returns:
        html.Div: The HTML representation of the trait.
    """
    return html.Div(
        [
            html.Span(title, className="card-element-label trait-label"),
            value,
        ],
        className="card-element card-element-value trait-value",
    )
