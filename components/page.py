"""Page class"""
from typing import Callable

from dash import html
from url_tools import convert

from components import main
from components.controls import control


class Page:
    """Represents a page on the dashboard and its associated information."""

    def __init__(
        self,
        title: str,
        html_template: list,
        controls: list[control.Control],
        update_function: Callable,
    ) -> None:
        """
        Args:
            title (str): Name of the page to display to the user
            html_template (list): List of HTML elements to make up the main content of the page.
            controls (list[control.Control]): List of Controls used on the page.
            update_function (Callable): Function to call when page needs to be updated
                due to user input.
        """
        self.title = title
        self.html_template = html_template
        self.update_function = update_function
        self.controls = controls

    def to_html(self, query_string: str) -> html.Main:
        """
        Creates the HTML needed to display the page, using the pages's template.

        Args:
            query_string (str): The query string containing information on controls.

        Returns:
            html.Main: The HTML main element containing the page's content.
        """
        kwargs = convert.query_string_to_kwargs(query_string)
        for user_control in self.controls:
            if user_control.identifier not in kwargs:
                kwargs[user_control.identifier] = user_control.default_value

        return main.main_content(
            [
                html.Div(
                    [
                        user_control.to_html(kwargs[user_control.identifier])
                        for user_control in self.controls
                    ],
                    hidden=True,
                )
            ]
            + self.html_template
        )

    def update(self, **control_values):
        """
        Updates the page with the specified control values.

        Args:
            **control_values: Arguments for controls with their associated values.
                May contain any controls, not just those for this page.

        Returns:
            list: List of the HTML elements to fill in the page.
        """
        relevant_controls = {
            key: value
            for key, value in control_values.items()
            if key in [user_control.identifier for user_control in self.controls]
        }

        return self.update_function(**relevant_controls)


class PageStorageAndLookup:
    """
    A container for dashboard pages, providing tools to store and find them.
    """

    def __init__(self) -> None:
        self.pages = {}
        self.homepage = None

    def add_page(self, url_path: str, page: Page) -> None:
        """
        Add a page to the store.

        Args:
            url_path(str): url path to page
            page (Page): The dashboard page to add.

        Raises:
            ValueError: If the URL path of the page is already in use.
        """

        if url_path in self.pages:
            raise ValueError(f"URL path: {url_path} already assigned to page.")

        self.pages[url_path] = page
        if not self.homepage:
            self.homepage = page

    def add_pages(self, pages: dict[str, Page]) -> None:
        """
        Add multiple pages at once to the store.

        Args:
            pages (dict[str,Page]): Dictionary of pages to add. Key should be the page's url path
                and value should be the page object.
        """
        for url_path, page in pages.items():
            self.add_page(url_path, page)

    def get_page(self, pathname: str) -> Page:
        """
        Find a stored page from its URL path.

        Args:
            pathname (str): The URL path to the page.

        Returns:
            Page: The associated dashboard page. None if no page found.
        """
        if pathname == "/" and self.homepage:
            return self.homepage
        if pathname in self.pages:
            return self.pages[pathname]
        return None
    
    def get_all_controls(self) -> list[control.Control]:
        controls = set()
        for _, page in self.pages.items():
            controls.update(page.controls)
        return list(controls)
