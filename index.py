"""
Index outlining the dashboard's layout and links to pages.
"""

from dash import Input, Output, State, dcc, html

import components as comp
import pages
import url_tools
from app import app

app.title = "D&D 5e Encounter Helper"

app.layout = html.Div(
    [
        comp.header(app.title),
        html.Div(
            [
                dcc.Location(id="url", refresh=False),
                html.Div([], id="page-content", className="page-content"),
            ],
            className="main-content-box",
        ),
    ]
)

dashboard_pages = comp.PageStorageAndLookup()

dashboard_pages.add_pages(
    {
        "/student-enrolment-timeseries": comp.Page(
            title="Monster Calculator",
            html_template=[
                comp.card_row(
                    comp.card(children=["Loading..."], element_id="react-content"),
                    stat_block = True
                ),
            ],
            controls=[
                comp.controls.ShortTexts.NAME,
                comp.controls.Sliders.CR,
                [comp.controls.Dropdowns.SIZE, comp.controls.Dropdowns.FAMILY],
                [comp.controls.Dropdowns.ARMOUR, comp.controls.Numbers.ARMOUR_BONUS],
            ],
            update_function=pages.update_monster_calculator,
        ),
    }
)


@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
    State("url", "search"),
)
def display_page(pathname, query_string):
    """Show the user the correct page for the given path"""
    page = dashboard_pages.get_page(pathname)

    if not page:
        raise ValueError(f"No page found for pathname '{pathname}'")

    nav_sidebar = comp.nav_sidebar(dashboard_pages, page, query_string)

    return [
        html.Div(
            [html.Div(nav_sidebar, id="nav_sidebar"), page.to_html(query_string)],
            className="dashboard-container",
        ),
    ]


@app.callback(
    Output("url", "search"),
    Output("nav_sidebar", "children"),
    Output("react-content", "children"),
    State("url", "pathname"),
    [
        Input(control.identifier, component_property="value")
        for control in dashboard_pages.get_all_controls()
    ],
)
def update_query_string(pathname, *control_values):
    """Update the query string in the url and in the navbar when a control is changed"""
    page = dashboard_pages.get_page(pathname)

    if not page:
        raise ValueError(f"No page found for pathname '{pathname}'")

    kwargs = {
        control.identifier: str(control_value)
        for control, control_value in zip(
            dashboard_pages.get_all_controls(), control_values
        )
    }

    query_string = url_tools.convert.kwargs_to_query_string(**kwargs)
    nav_sidebar = comp.nav_sidebar(dashboard_pages, page, query_string)

    content = page.update(**kwargs)

    return query_string, nav_sidebar, content
