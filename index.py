"""
Index outlining the dashboard's layout and links to pages.
"""

import json
from dash import Input, Output, State, dcc, html

import components as comp
import pages
import url_tools
from dnd import monster
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
                    [
                        comp.card(
                            [comp.button("Save Monster", component_id="save-button", width="200px")]
                        ),
                        comp.card([""], element_id="save-message"),
                    ]
                ),
                html.Div(['Loading...'], id='react-content'),
            ],
            controls={
                "Basics": [
                    comp.controls.ShortTexts.NAME,
                    comp.controls.Sliders.CR,
                    [comp.controls.Dropdowns.SIZE, comp.controls.Dropdowns.FAMILY],
                ],
                "Armour": [
                    [comp.controls.Dropdowns.ARMOUR, comp.controls.Numbers.ARMOUR_BONUS]
                ],
                "Speed": [
                    [
                        comp.controls.Numbers.BASIC_SPEED,
                        comp.controls.Numbers.FLYING,
                        comp.controls.Numbers.HOVERING,
                        comp.controls.Numbers.BURROWING,
                        comp.controls.Numbers.CLIMBING,
                        comp.controls.Numbers.SWIMMING,
                    ]
                ],
                "Attribute Modifiers": [
                    [
                        comp.controls.Numbers.STR,
                        comp.controls.Numbers.DEX,
                        comp.controls.Numbers.CON,
                        comp.controls.Numbers.INT,
                        comp.controls.Numbers.WIS,
                        comp.controls.Numbers.CHA,
                    ]
                ],
                "Traits": [comp.controls.TextArea.TRAITS],
            },
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

    query_string = url_tools.convert_query.kwargs_to_query_string(**kwargs)
    nav_sidebar = comp.nav_sidebar(dashboard_pages, page, query_string)

    content = page.update(**kwargs)

    return query_string, nav_sidebar, content


@app.callback(
    Output("save-message", "children"),
    Input("save-button", "n_clicks"),
    [
        State(control.identifier, component_property="value")
        for control in dashboard_pages.get_all_controls()
    ],
)
def save_monster(n_clicks, *control_values):
    """
    Save the current monster to a json file.
    """
    if not n_clicks:
        return ""

    monster_to_save = monster.Monster.from_query_string_kwargs(
        **{
            control.identifier: str(control_value)
            for control, control_value in zip(
                dashboard_pages.get_all_controls(), control_values
            )
        }
    )

    with open(
        f'data/monsters/{monster_to_save.core.name.replace(" ", "_")}.json',
        mode="w",
        encoding="utf-8",
    ) as outfile:
        json.dump(monster_to_save.to_dict(), indent=4, sort_keys=True, fp=outfile)

    return f'{monster_to_save.core.name.replace(" ", "_")}.json saved.'
