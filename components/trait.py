from dash import html


def trait(title: str, value: str):
    return html.Div(
        [
            html.Span(title, className="card-element-label trait-label"),
            value,
        ],
        className="card-element card-element-value trait-value",
    )
