"""Format challenge rating function"""
from typing import Union

import formatting


def format_challenge_rating(challenge_rating: Union[int, str], /) -> str:
    """
    Formats the internal challenge rating value as a valid D&D challenge rating.
    Internally, the challenge rating is an integer between -3 and 30.
    For values below 0, we want to display as relevant fraction to the user.

    Args:
        challenge_rating (Union[int, str]): Internal challenge rating

    Returns:
        str: Formatted challenge rating for display
    """
    formatted_challenge_rating = str(challenge_rating)
    if formatting.is_intlike(challenge_rating) and int(challenge_rating) < 0:
        formatted_challenge_rating = f"1\u2044{2 ** -int(challenge_rating)}"
    return formatted_challenge_rating
