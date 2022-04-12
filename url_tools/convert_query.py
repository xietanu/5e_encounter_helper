"""Functions to convert between query string and kwargs"""

from urllib import parse


def kwargs_to_query_string(**kwargs) -> str:
    """
    Contvert keyword arguments to query string

    Returns:
        str: URL encoded query string
    """
    return "?" + parse.urlencode(kwargs)


def query_string_to_kwargs(query_string: str) -> dict:
    """
    Convert query string to keyword arguments.

    Args:
        query_string (str): URL encoded query string

    Returns:
        dict: Keyword arguments
    """
    if query_string.startswith("?"):
        query_string = query_string[1:]
    return parse.parse_qs(query_string)
