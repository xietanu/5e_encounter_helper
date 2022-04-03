"""Components for a navigation sidebar"""

from dash import html, dcc
from components import page


def nav_sidebar(
    dashboard_pages: page.PageStorageAndLookup,
    current_page: page.Page,
    query_string: str,
) -> html.Nav:
    """
    Creates a navigation sidebar component with links to the specified pages.

    Args:
        dashboard_pages (PageStorageAndLookup): Container of the dashboard pages.
        current_page (Page): The current page being displayed.
        query_string (str): The query string for the current filters.

    Returns:
        html.Nav: The navigation sidebar component.
    """
    return html.Nav(
        html.Ul(
            [
                html.Li(
                    dcc.Link(
                        page.title,
                        href=url_path + query_string,
                        className="nav_sidebar_link",
                    ),
                    className="active_item" if page is current_page else "",
                )
                for url_path, page in dashboard_pages.pages.items()
            ],
        ),
        role="navigation",
        className="nav_sidebar",
    )
