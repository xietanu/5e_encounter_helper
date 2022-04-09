"""Functions to test types"""
from typing import Any


def is_intlike(value: Any, /) -> bool:
    """
    Test if a value can be converted to an integer.

    Args:
        value (Any): Value to test

    Returns:
        bool: If it can be safely converted.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False
