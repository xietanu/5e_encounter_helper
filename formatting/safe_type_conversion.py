"""Functions to safely convert values"""
from formatting.type_test import is_intlike


def defaulted_int(value, /, default: int) -> int:
    """
    Returns the integer interpretation of the value if possible,
    otherwise returns the default value

    Args:
        value (any): Any value
        default (int): Default integer value

    Returns:
        int: The converted value / default value
    """
    return int(value) if is_intlike(value) else default
